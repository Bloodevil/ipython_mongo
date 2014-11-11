from IPython import get_ipython
from imongo.imongo import MongoDB
from nose import with_setup

ip = get_ipython()
mongo = 'localhost'

def setup():
    imongo = MongoDB(shell=ip)
    ip.register_magics(imongo)

def test_magic_find():
    assert ip.find_line_magic('show_dbs') != None
    assert ip.find_line_magic('show_collections') != None
    assert ip.find_line_magic('help') != None
    assert ip.find_line_magic('print') != None
    assert ip.find_line_magic('insert') != None

def test_magic_not_found():
    assert ip.find_line_magic('test') == None

def test_show_dbs_error():
    assert ip.run_line_magic('show_dbs', '') == "[ERROR] please connect to mongodb using %mongo_connect"

def test_show_collections_error():
    assert ip.run_line_magic('show_collections', '') == '[ERROR] usage %show_collections <dbname>'
    assert ip.run_line_magic('show_collections', 'test') == '[ERROR] connect mongodb before %show_collections'

def test_insert_error():
    assert ip.run_line_magic('insert', '') == '[ERROR] connect mongodb before %insert'

def test_print_error():
    assert ip.run_line_magic('print', '') == '[ERROR] connect mongodb before %print'

def _init():
    ip.run_line_magic('mongo_connect', mongo)
    ip.run_line_magic('insert', "ipython.test {'test': 1}")

def _teardown():
    ip.run_cell("conn = %mongo_connect %s", mongo)
    ip.runcode("conn.ipython.test.drop()")
    ip.run_line_magic('drop', "ipython")

@with_setup(_init, _teardown)
def test_show_dbs():
    assert 'ipython' in ip.run_line_magic('show_dbs', '')


