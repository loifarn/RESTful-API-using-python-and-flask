# RESTful API using python and flask

<div>
  <img src="https://imgur.com/2cOTPr8.png" width="150">
  <img src="https://imgur.com/GAxd0mc.png" width="150">
  <img src="https://imgur.com/MyAUhjI.png" width="150">
  <img src="https://imgur.com/AaMyoVm.png" width="150">
</div>

<br>

## What is it?
This is a basic example of how you can set up a RESTful API.
* server.py: The main server component that
  * Creates the app
  * Connects to the database
  * and configure accecible routes
  
* Classes: Used to pull data from the database and serve as a resource for the flask_restful api
  * Employees returns employees from the sample database
  * EmployeeId returns an employee based on his id
  * Tracks returns data for stored tracks (songs)

## Credits
* Sample database used: http://www.sqlitetutorial.net/sqlite-sample-database/
* Flask: http://flask.pocoo.org/
* Flask Restful: https://flask-restful.readthedocs.io/en/latest/
* SQL Alchemy: https://www.sqlalchemy.org/
