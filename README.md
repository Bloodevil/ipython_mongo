ipython mongo magic
=============

    :Info: ipython mongo shell extension
    :Author: Yeaji Shin ( yeahjishin@gmail.com )


Install
=======

use github:
    In [1]: %install_ext https://github.com/Bloodevil/ipython_mongo/edit/master/imongo.py
    In [2]: %load_ext imongo.py

    git clone https://github.com/Bloodevil/ipython_mongo.git
    cd ipython_mongo
    python setup.py install

use pip:

    pip install ipython_mongo
    In [1]: %load_ext imongo

import error when load_ext
=============

1. check sys.path 
2. check imongo under '/usr/lib/python2.7/dist-packages/IPython/extensions'

Usage
=============

%mongo_connect [mongodb://localhost:27017]
```sql
In [1]: con = %mongo_connect

In [2]: con
Out[2]: MongoClient('localhost', 27017)

In [3]: %mongo_connect mongodb://127.0.0.1:27017
Out[3]: MongoClient(u'127.0.0.1', 27017)
```

%show_dbs
```sql
In [10]: %show_dbs
Out[10]: 
[u'local',
 u'tumblr',
 u'admin',
 u'movie',
 u'theater',
 u'a',
 u'daa',
 u'dbs',
 u'test']
```

%show_collections [dbname]
```sql
In [11]: %show_collections movie
Out[11]: [u'system.indexes', u'kobis']
```

%insert db.collection {data}
```sql
In [29]: %insert test.test {"test": "test1"}
{u'test': u'test1'}

In [31]: conn.test.test.find_one()
Out[31]: {u'_id': ObjectId('544a20e5eb5e7b1ccdb7ca54'), u'test': u'test'}
```

