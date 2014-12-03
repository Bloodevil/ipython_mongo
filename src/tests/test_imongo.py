from IPython import get_ipython
from imongo.imongo import MongoDB
from nose import with_setup

ip = get_ipython()
mongo = '127.0.0.1'

def setup():
    imongo = MongoDB(shell=ip)
    ip.register_magics(imongo)

def test_magic_find():
    assert ip.find_line_magic('show_dbs') != None
    assert ip.find_line_magic('show_collections') != None
    assert ip.find_line_magic('help') != None
    assert ip.find_line_magic('print') != None
    assert ip.find_line_magic('insert') != None
    assert ip.find_line_magic('find') != None

def test_magic_not_found():
    assert ip.find_line_magic('test') == None
    assert ip.find_line_magic('note_exist') == None

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
    ip.run_line_magic('insert', "imongo.test {'test': 1}")

def _teardown():
    ip.run_line_magic('drop', "imongo")

@with_setup(_init, _teardown)
def test_show_dbs():
    assert 'imongo' in ip.run_line_magic('show_dbs', '')
    assert 'test' in ip.run_line_magic('show_collections', 'imongo')

def _init_find():
    ip.run_line_magic('mongo_connect', mongo)

# mongodb shell server core js test find1.js
@with_setup(_init_find)
def test_find1():
    ip.run_line_magic('insert', "imongo.find1 { 'a':1, 'b': 'hi' }")
    ip.run_line_magic('insert', "imongo.find1 { 'a':2, 'b': 'hi' }")

    assert ip.run_line_magic('find', 'imongo.find1 {}')[0]['a'] == 1
    q = ip.run_line_magic('find', 'imongo.find1 {}')[0]
    q['c'] = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    ip.run_line_magic('insert', 'imongo.find1 ' + str(q))
    assert ip.run_line_magic('find', 'imongo.find1 {}')[0]['a'] == 1
    assert ip.run_line_magic('find', "imongo.find1 {'a':1}")[0]['b'] != None
    _teardown()


# mongodb shell server core js test find2.js
@with_setup(_init_find, _teardown)
def test_find2():
    for x in xrange(3):
        ip.run_line_magic('insert', "imongo.find2 {}")

    f = ip.run_line_magic('find', 'imongo.find2 {}')
    assert f[0]['_id'] < f[1]['_id']
    assert f[1]['_id'] < f[2]['_id']


def test_find3():
    for x in xrange(50):
        ip.run_line_magic('insert', "imongo.find3 { 'a' : %s }"%x)

    f = ip.run_line_magic('find', 'imongo.find3 {}')
    # f = ip.run_line_magic('find 20', 'imongo.find3 {}') limit 20
    assert f.__len__() == 50

