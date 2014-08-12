ipython mongo magic
=============

```sql
In [1]: %install_ext https://github.com/Bloodevil/ipython_mongo/edit/master/imongo.py
In [2]: %load_ext imongo.py
```

import error when load_ext
=============

1. check sys.path 
2. check imongo under '/usr/lib/python2.7/dist-packages/IPython/extensions'

Usage
=============

```sql
In [84]: con = %mongo_connect

In [85]: con
Out[85]: Connection('localhost', 27017)
```
