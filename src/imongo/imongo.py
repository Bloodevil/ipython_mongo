from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from IPython.core.magic import Magics, magics_class, cell_magic, line_magic, needs_local_scope
from IPython.config.configurable import Configurable
from helps import *
from util import parse, print_json, print_cursor, find_query_pymongo, insert_query_pymongo


@magics_class
class MongoDB(Magics, Configurable):
    _conn = None

    def __init__(self, shell):
        Configurable.__init__(self, config=shell.config)
        Magics.__init__(self, shell=shell)
        self.shell.configurables.append(self)

    @line_magic('mongo_connect')
    def conn(self, line):
        """Conenct to mongo database in ipython shell.
        Examples::
            %mongo_connect
            %mongo_connect mongodb://hostname:port
        """
        if line:
            uri = line
        else:
            uri = 'mongodb://127.0.0.1:27017'
        self._conn = MongoClient(uri)
        # add db and collection property to object for autocomplete.
        for db in self._conn.database_names():
            setattr(self._conn, db, Database(self._conn, db))
            _db = Database(self._conn, db)
            for collection in _db.collection_names():
                # [TODO] change eval to other!!
                setattr(eval('self._conn.'+db), collection,
                        Collection(_db, collection))
        return self._conn

    @line_magic('show_dbs')
    def show_dbs(self, line):
        if self._conn:
            print('Pymongo> MongoClient(url).database_names()') # [TODO]
            return self._conn.database_names()
        else:
            return "[ERROR] please connect to mongodb using %mongo_connect"

    @line_magic('show_collections')
    def show_collections(self, line):
        if not line:
            return "[ERROR] usage %show_collections <dbname>"
        if not self._conn:
            return "[ERROR] connect mongodb before %show_collections"
        if self._conn and line:
            print("Pymongo> Database(%s, %s).collection_names()"%(str(self._conn), line))
            collections = Database(self._conn, line).collection_names()
        if not collections:
            print("[ERROR] check your database name there no collection")
            collections = self.show_dbs(self)
        return collections

    @needs_local_scope
    @line_magic('insert')
    @cell_magic('insert')
    def insert(self, line, cell='', local_ns={}):
        if not self._conn:
            return "[ERROR] connect mongodb before %insert"
        parsed = parse('%s\n%s' % (line, cell), self)
        try:
            data = insert_query_pymongo(parsed['data'])
            parsed['collection'].insert(data)
        except Exception as e:
            return "[ERROR] fail to insert data", e

    @line_magic('drop')
    @cell_magic('drop')
    def drop(self, line):
        if not self._conn:
            return "[ERROR] connect mongodb before %delete"
        if not line:
            return "[ERROR] please use like %delete db.collection or %delete db"
        db_col = line.split('.')
        if db_col.__len__() > 2:
            return "[ERROR] please use like %delete db.collection or %delete db"
        elif db_col.__len__() == 2:
            Database(self._conn, db_col[0]).drop_collection(db_col[1])
        else:
            self._conn.drop_database(db_col[0])

    @line_magic('print')
    @cell_magic('print')
    def mongo_print(self, line, cell=''):
        if not self._conn:
            return "[ERROR] connect mongodb before %print"
        parsed = parse('%s\n%s' % (line, cell), self)
        # print db.collection.find()
        try:
            result = print_json(parsed['data'])
        except Exception:
            return "[ERROR] fail to print about", parsed['data']

    @line_magic('find')
    @cell_magic('find')
    def mongo_find(self, line, cell=''):
        if not self._conn:
            return "[ERROR] connect mongodb before %find"
        parsed = parse('%s\n%s' % (line, cell), self)
        try:
            query = find_query_pymongo(parsed['data'])
            return print_cursor(parsed['collection'].find(query))
        except Exception as e:
            return "[ERROR] fail to query ", e

    @line_magic('help')
    def help_message(self, line):
        message = ''
        if line == 'db':
            message += DB_METHODS
        elif line == 'collection':
            message += COLLECTION_METHODS
        else:
            message += HELP_MESSAGE
        print(message)


def load_ipython_extension(ipython):
    ipython.register_magics(MongoDB)
