import pymongo
from IPython.core.magic import Magics, magics_class, line_magic, cell_magic

@magics_class
class MongoDB(Magics):
    @line_magic('mongo_connect')
    def conn(self, line, host="localhost",  port=27017):
        return pymongo.connection.Connection(host, port)

    @magic_arguments()
    @argument(
        'conn',
        help="`pymongo.connection.Connection` object."
    )

def load_ipython_extension(ipython):
    """Load the extension in IPython."""
    ipython.register_magics(MongoDB)

