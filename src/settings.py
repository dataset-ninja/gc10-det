from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "GC10-DET"
PROJECT_NAME_FULL: Optional[str] = "GC10-DET: Metallic Surface Defect Detection"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0(source_url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7146379/pdf/sensors-20-01562.pdf")
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Domain.SurfaceDefectDetection()]
CATEGORY: Category = Category.Manufacturing()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2020-03-11"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://www.kaggle.com/datasets/alex000kim/gc10det"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 392667
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/gc10-det"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://www.kaggle.com/datasets/alex000kim/gc10det/download?datasetVersionNumber=1"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "punching_hole": [230, 25, 75],
    "welding_line": [255, 225, 25],
    "crescent_gap": [0, 130, 200],
    "water_spot": [245, 130, 48],
    "oil_spot": [145, 30, 180],
    "silk_spot": [70, 240, 240],
    "inclusion": [240, 50, 230],
    "rolled_pit": [210, 245, 60],
    "crease": [250, 190, 212],
    "waist folding": [0, 128, 128],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[
    str
] = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7146379/pdf/sensors-20-01562.pdf"
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {"GitHub":"https://github.com/lvxiaoming2019/GC10-DET-Metallic-Surface-Defect-Datasets"}

CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = ["Xiaoming Lv", "Fajie Duan", "Jia-jia Jiang", "Xiao Fu", "Lin Gan"]
AUTHORS_CONTACTS: Optional[List[str]] = ["fjduan@tju.edu.cn"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Tianjin University, China"
ORGANIZATION_URL: Optional[
    Union[str, List[str]]
] = r"https://www.tsinghua.edu.cn/dpien/info/1092/1039.htm#:~:text=03%20Views%3A%20954-,The%20State%20Key%20Laboratory%20of%20Precision%20Measurement%20Technology%20and%20Instruments,to%20the%20public%20in%201995."

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS    
    settings["repository"] = REPOSITORY    
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
