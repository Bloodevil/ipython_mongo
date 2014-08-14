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

%mongo_connect <mongodb://localhost:27017>
===
```sql
In [1]: con = %mongo_connect

In [2]: con
Out[2]: MongoClient('localhost', 27017)

In [3]: %mongo_connect mongodb://127.0.0.1:27017
Out[3]: MongoClient(u'127.0.0.1', 27017)
```

%show_dbs
===
```sql
In [10]: %show_dbs
Out[10]: 
[u'local',
 u'tumblr',
 u'admin',
 u'kobis',
 u'movie',
 u'theater',
 u'a',
 u'cine_db',
 u'daa',
 u'dbs',
 u'test']
```

%show_collections
===
```sql
In [11]: %show_collections movie
Out[11]: [u'system.indexes', u'kobis']
```



