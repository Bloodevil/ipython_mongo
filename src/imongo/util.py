from pymongo.collection import Collection
from pymongo.database import Database
import re


def parse(cell, config):
    parts = [part.strip() for part in cell.split(None, 1)]
    if not parts:
        return """[ERROR] please enter the db.collection and data
            %insert db.collection {data} or [{data}, {data}...]
            or
            %%insert db.collection
            {data} or [{data}, {data} ...]"""
    db, col = parts[0].split('.')
    if not db and not col:
        return """[ERROR] please enter the db and collection name both of all
            %insert db.collection {data or data list}
            or
            %%insert db.collection
            {data or data list}"""
    _db = Database(config._conn, db)
    _col = Collection(_db, col)
    data = parts[1] if len(parts) > 1 else ''
    return {'collection': _col, 'data': data.strip()}


def print_json():
    return None


def print_cursor(result):
    return list(result)

"""
in mongo shell
- {'name': /sometext/} -> {'name': {'$regex': 'sometext'}}
- {name: /^pa/} -> {name: {$regex:^pa}}
- {name: /ro$/} -> {name: {$regex:ro$}}

more easily
- %find db.collection 3 < "field" < 10 -> {"field": { $lt : 10, $gt : 3 }}
- %find db.collection 3 < "field" -> {"field": { $gt : 3 }}
"""

def replace_slash(query):
    slash_list = []
    for i, q in enumerate(query):
        if q == '/':
            if i == 0:
                slash_list.append(i)
                continue
            if query[i-1] != '\\':
                slash_list.append(i)
    if slash_list.__len__() %2 == 1:
        raise "[ERROR] please check your find query about slash pair"
    regex_query = "{'$regex': '%s'}"
    replace_list = []
    for index in xrange(slash_list.__len__()/2):
        replace_list.append(query[slash_list[index*2]:slash_list[index*2+1]+1])
    for r in replace_list:
        query = query.replace(r, regex_query%r[1:-1])
    return query

def query_pymongo(raw_query):
    query = replace_slash(raw_query)
    return query
