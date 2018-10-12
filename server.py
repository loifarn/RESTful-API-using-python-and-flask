from flask import Flask
from flask_restful import Api
from sqlalchemy import create_engine
from classes import Employees, EmployeesName, Tracks

# Create database connection and app
db = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


# Sets database for the chosen object.
def set_db(obj):
    obj.db = db
    return obj


# Default route
@app.route('/')
def hello():
    return "Root page of example RESTful API"


# Routing
api.add_resource(set_db(Employees.Employees), '/employees')
api.add_resource(set_db(EmployeesName.EmployeesName), '/employees/<employee_id>')
api.add_resource(set_db(Tracks.Tracks), '/tracks')


# Start
if __name__ == '__main__':
     app.run(port='8080')