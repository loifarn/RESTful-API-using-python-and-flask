from flask_restful import Resource
from flask_jsonpify import jsonify


class Tracks(Resource):
    db = None

    def __init__(self, database):
        self.db = database

    def get(self):
        conn = self.db.connect()
        query = conn.execute("select trackid, name, composer and unit price from tracks;")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)