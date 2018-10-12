from flask_restful import Resource


class Employees(Resource):
    db = None

    def __init__(self, database):
        self.db = database

    def get(self):
        conn = self.db.connect()
        query = conn.execute("select * from employees")
        return {'employees': [i[0] for i in query.cursor.fetchall()]}