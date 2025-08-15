Dataset **GC10-DET** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTAwOF9HQzEwLURFVC9nYzEwLWRldC1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJaM2JTWlhTcE9TQjVONFRWVklLWG1IWGR2NTNQbWJGZG1vUFJWSXlIZlI4PSJ9?response-content-disposition=attachment%3B%20filename%3D%22gc10-det-DatasetNinja.tar%22)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='GC10-DET', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/alex000kim/gc10det/download?datasetVersionNumber=1).