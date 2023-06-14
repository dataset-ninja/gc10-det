Dataset **GC10-DET** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/L/I/OE/eCmrVlWp164QdKO8SS8VxiAqHHKpd88Afrbap1qtbSnqvSIG3uz15lsz7CWnFk1hNlh9Fsn6Q2tLThzi4VT3tTk6D3m9DFjiyLTeA1gcOCJYOtuP2EMK2rAwa0rt.tar)

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