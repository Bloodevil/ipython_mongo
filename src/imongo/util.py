from pymongo.collection import Collection
from pymongo.database import Database
import json


"""
[TODO] - {test: 1}  -> dict {'test': 1}
- {'test': 1} -> dict {'test': 1}
- {"test": 1} -> dict {'test': 1}
"""
def dictize(query):
    dictionary = json.loads(query.replace("'", '"'))
    return dictionary


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
    data = parts[1].strip() if len(parts) > 1 else ''
    return {'collection': _col, 'data': data}


def print_json():
    return None


def print_cursor(result):
    return list(result)


"""
in mongo shell
- {'name': /sometext/} -> {'name': {'$regex': 'sometext'}}
- {name: /^pa/} -> {name: {$regex: '^pa'}}
- {name: /ro$/} -> {name: {$regex: 'ro$'}}

more easily
- %find db.collection {'field': > 3} -> {"field": { $gt : 3 }}
- %find db.collection {'field': < 10} -> {"field": { $lt : 10 }}
- %find db.collection {'field': <= 10} -> {"field": { $lte : 10 }}
- %find db.collection {'field': < 10, 'field': >= 5} ->
                      {"field": { $lt : 10, $gte : 5 }}
"""
def query_parser(query):
    tmp_query = query.replace('{', '').replace('}', '').strip()
    if not tmp_query:
        return '{}'
    token_dict = {}
    for q in tmp_query.split(','):
        k, v = q.split(':', 1)
        token_dict[k] = v
    parsed_token = {}
    for field, data in token_dict.iteritems():
        field = str(field.strip())
        data = data.strip()
        if not data:
            # [TODO] add not exist query.
            continue
        data = replace_slash(data)
        data = replace_comp(data)
        if not field in parsed_token.keys():
            parsed_token.setdefault(field, data)
        if type(data) == dict:
            parsed_token.setdefault(field, dict(parsed_token[field], **data))
        else:
            parsed_token.setdefault(field, data)
    parsed_query = '{'
    parsed_query += ','.join(field+':'+str(data) for field, data in parsed_token.iteritems())
    parsed_query += '}'
    return parsed_query


def cast_type(data):
    try:
        data = int(data)
    except:
        data = str(data)
    return data


# [TODO] change starts with
def replace_comp(data):
    if data[0:2] in ['<=', '>=']:
        op = data[0:2]
        query = cast_type(data[2:].strip())
        if op == '>=':
            data = {'$gte': query}
        elif op == '<=':
            data = {'$lte': query}
    if data[0] in ['<', '>']:
        op = data[0]
        query = cast_type(data[1:].strip())
        if op == '<':
            data = {'$lt': query}
        elif op == '>':
            data = {'$gt': query}
    return data


# query -> data
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


def find_query_pymongo(raw_query):
    query = query_parser(raw_query)
    query = dictize(query)
    return query


def insert_query_pymongo(raw_query):
    query = dictize(raw_query)
    return query
