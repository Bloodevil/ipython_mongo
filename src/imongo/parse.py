from pymongo.collection import Collection
from pymongo.database import Database

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
    return {'collection': _col, 'data' : data.strip()}
