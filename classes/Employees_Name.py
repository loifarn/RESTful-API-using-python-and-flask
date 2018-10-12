from flask_restful import Resource
from flask_jsonpify import jsonify


class Employees_Name(Resource):
    db = None

    def __init__(self, database):
        self.db = database

    def get(self, employee_id):
        conn = self.db.connect()
        query = conn.execute("select * from employees where EmployeeId =%d " % int(employee_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)