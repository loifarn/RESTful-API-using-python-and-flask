from flask_restful import Resource
from flask_jsonpify import jsonify


class Tracks(Resource):
    def get(self):
        conn = self.db.connect()
        query = conn.execute("select trackid, name, composer and unitprice from tracks;")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)
