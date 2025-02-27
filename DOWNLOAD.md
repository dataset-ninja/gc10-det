Dataset **GC10-DET** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzEwMDhfR0MxMC1ERVQvZ2MxMC1kZXQtRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiS3JGOFYzSllPOXV4TXk0dFIzdHJMb01ORGU5R2wzKzMyQVY2UmRKUmVQVT0ifQ==)

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