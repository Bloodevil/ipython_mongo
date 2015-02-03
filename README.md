<img src="https://travis-ci.org/Bloodevil/ipython_mongo.svg?branch=master"/>

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
Pymongo> MongoClient(url).database_names()
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

%drop db.collection
%drop db


%find imongo.find1 {data}
```sql
In [9]: %find imongo.find1 {}
Out[9]: [{u'_id': ObjectId('546d7192eb5e7b1cfbdf12cb'), u'test': u'abcdef'}]

In [10]: %find imongo.find1 {'test': /c/}
Out[10]: [{u'_id': ObjectId('546d7192eb5e7b1cfbdf12cb'), u'test': u'abcdef'}]

In [11]: %find imongo.find1 {'test': /^a/}
Out[11]: [{u'_id': ObjectId('546d7192eb5e7b1cfbdf12cb'), u'test': u'abcdef'}]

In [17]: %find imongo.find1 {'test': /f$/}
Out[17]: [{u'_id': ObjectId('546d7192eb5e7b1cfbdf12cb'), u'test': u'abcdef'}]

In [21]: %find imongo.find1 {'test': > 120}
Out[21]:
[{u'_id': ObjectId('546d71f4eb5e7b1cfbdf12cc'), u'test': 123},
 {u'_id': ObjectId('546d71fbeb5e7b1cfbdf12ce'), u'test': 1920}]

In [22]: %find imongo.find1 {'test': < 120}
Out[22]: [{u'_id': ObjectId('546d71f7eb5e7b1cfbdf12cd'), u'test': 100}]

In [7]: %find imongo.find1 {'test': <= 100}
Out[7]: [{u'_id': ObjectId('546d71f7eb5e7b1cfbdf12cd'), u'test': 100}]

In [3]: %find imongo.find1 {'test': > 120, 'test': < 1000 }
Out[3]: [{u'_id': ObjectId('546d71f4eb5e7b1cfbdf12cc'), u'test': 123}]
```

%find_one imongo.find1 {data}

%count imongo.find1
50

