Dataset **GC10-DET** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/V/7/Ka/XH4YwBZOVaQA9zFLTv1FkLIX8hBPK4DMx16qky6d34b0gu7ZUgnFrwb4dnYSkmcsIQMW2rBY7O73A93gCgoGNUxj2OBNPaHojny9bQTYHk9KsztIyNO5AE9HEODU.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='GC10-DET', dst_path='~/dtools/datasets/GC10-DET.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/alex000kim/gc10det/download?datasetVersionNumber=1)