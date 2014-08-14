import pymongo
from IPython.core.magic import Magics, magics_class, line_magic

@magics_class
class MongoDB(Magics):
    _conn = None
    @line_magic('mongo_connect')
    def conn(self, line, host="localhost",  port=27017):
        self._conn = pymongo.connection.Connection(host, port)
        return self._conn

    @line_magic('show_dbs')
    def show_dbs(self, line):
        if self._conn:
            return self._conn.database_names()
        else:
            print "please connect to mongodb using %mongo_connect"
            return line

def load_ipython_extension(ipython):
    ipython.register_magics(MongoDB)

