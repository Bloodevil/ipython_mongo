from IPython import get_ipython
from imongo.imongo import MongoDB

ip = get_ipython()

def setup():
    imongo = MongoDB(shell=ip)
    ip.register_magic(imongo)

def _init():
    ip.run_line_magic('mongo_connect')
    ip.run_line_magic('insert', "ipython.test {'test': 1}")

def _teardown():
    ip.run_cell("conn = %mongo_connect")
    ip.runcode("conn.ipython.test.drop()")
    #ip.run_line_magic('delete', "ipython.test")
