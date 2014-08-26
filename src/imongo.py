from pymongo import MongoClient
from pymongo.database import Database
from IPython.core.magic import Magics, magics_class, line_cell_magic, line_magic

@magics_class
class MongoDB(Magics):
    _conn = None
    @line_magic('mongo_connect')
    def conn(self, line):
        if line:
            uri = line
        else:
            uri = 'mongodb://localhost:27017'
        self._conn = MongoClient(uri)
        return self._conn

    @line_magic('show_dbs')
    def show_dbs(self, line):
        if self._conn:
            return self._conn.database_names()
        else:
            print "[ERROR] please connect to mongodb using %mongo_connect"
            return line

    @line_magic('show_collections')
    def show_collections(self, line):
        if self._conn and line:
            collections = Database(self._conn, line).collection_names()
        if not line:
            return "[ERROR] usage %show_collections <dbname>"
        if not self._conn:
            return "[ERROR] connect mongodb before %show_collections"
        if not collections:
            print "[ERROR] check your database name there no collection"
            collections = self.show_dbs(self)
        return collections

def load_ipython_extension(ipython):
    ipython.register_magics(MongoDB)

