# https://www.kaggle.com/datasets/alex000kim/gc10det

import os, glob
import numpy as np
import supervisely as sly
from supervisely.io.fs import get_file_name_with_ext, get_file_name, file_exists
import xml.etree.ElementTree as ET
from dotenv import load_dotenv


# # if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()

# project_name = "GC10-DET"
dataset_path = "./APP_DATA/archive"
batch_size = 30
ds_name = "ds0"
anns_folder = "lable"


def create_ann(image_path):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]

    ann_path = os.path.join(dataset_path, anns_folder, get_file_name(image_path) + ".xml")
    if file_exists(ann_path) is False:
        return sly.Annotation(img_size=(image_np.shape[0], image_np.shape[1]))

    tree = ET.parse(ann_path)
    root = tree.getroot()
    objects_content = root.findall(".//object")
    for obj_data in objects_content:
        name = obj_data.find(".//name").text
        truncated = obj_data.find(".//truncated").text
        bndbox = obj_data.find(".//bndbox")
        top = int(bndbox.find(".//ymin").text)
        left = int(bndbox.find(".//xmin").text)
        bottom = int(bndbox.find(".//ymax").text)
        right = int(bndbox.find(".//xmax").text)

        rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
        obj_class = name_to_obj_class.get(name[:2])
        if obj_class is None:
            continue
        label = sly.Label(rectangle, obj_class)
        if truncated == "1":
            tag = sly.Tag(meta=tag_meta)
            label = sly.Label(rectangle, name_to_obj_class[name[:2]], tags=[tag])
        labels.append(label)

    return sly.Annotation(img_size=(image_np.shape[0], image_np.shape[1]), labels=labels)


obj_class_punching_hole = sly.ObjClass("punching_hole", sly.Rectangle)
obj_class_welding_line = sly.ObjClass("welding_line", sly.Rectangle)
obj_class_crescent_gap = sly.ObjClass("crescent_gap", sly.Rectangle)
obj_class_water_spot = sly.ObjClass("water_spot", sly.Rectangle)
obj_class_oil_spot = sly.ObjClass("oil_spot", sly.Rectangle)
obj_class_silk_spot = sly.ObjClass("silk_spot", sly.Rectangle)
obj_class_inclusion = sly.ObjClass("inclusion", sly.Rectangle)
obj_class_rolled_pit = sly.ObjClass("rolled_pit", sly.Rectangle)
obj_class_crease = sly.ObjClass("crease", sly.Rectangle)
obj_class_waist_folding = sly.ObjClass("waist folding", sly.Rectangle)

name_to_obj_class = {
    "1_": obj_class_punching_hole,
    "2_": obj_class_welding_line,
    "3_": obj_class_crescent_gap,
    "4_": obj_class_water_spot,
    "5_": obj_class_oil_spot,
    "6_": obj_class_silk_spot,
    "7_": obj_class_inclusion,
    "8_": obj_class_rolled_pit,
    "9_": obj_class_crease,
    "10": obj_class_waist_folding,
}
obj_class_collection = sly.ObjClassCollection(
    [
        obj_class_punching_hole,
        obj_class_welding_line,
        obj_class_crescent_gap,
        obj_class_water_spot,
        obj_class_oil_spot,
        obj_class_silk_spot,
        obj_class_inclusion,
        obj_class_rolled_pit,
        obj_class_crease,
        obj_class_waist_folding,
    ]
)

tag_meta = sly.TagMeta("truncated", sly.TagValueType.NONE)
tag_metas = sly.TagMetaCollection([tag_meta])

def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_class_collection, tag_metas=tag_metas)
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_pathes = glob.glob(dataset_path + "/*/*.jpg")
    unique_images_pathes = []
    unique_images_names = []
    for image_path in images_pathes:
        image_name = get_file_name(image_path)
        if image_name not in unique_images_names:
            unique_images_names.append(image_name)
            unique_images_pathes.append(image_path)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(unique_images_pathes))

    for img_pathes_batch in sly.batched(unique_images_pathes, batch_size=batch_size):
        images_names_batch = [get_file_name_with_ext(image_path) for image_path in img_pathes_batch]

        anns_batch = [create_ann(image_path) for image_path in img_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        api.annotation.upload_anns(img_ids, anns_batch)

        progress.iters_done_report(len(images_names_batch))

    return project