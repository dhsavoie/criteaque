from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


admins = Blueprint('admins', __name__)

# this is a route for listing all of the departments
@admins.route('/get_majors', methods=['GET'])
def get_majors():
    cursor = db.get_db().cursor()  # get a cursor object from the database
    cursor.execute('select Major from Major')  # get all department names
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response  # return the data as a JSON response

# this is a route for listing all of the departments
@admins.route('/get_departments', methods=['GET'])
def get_departments():
    cursor = db.get_db().cursor()  # get a cursor object from the database
    # get all department names
    cursor.execute('select DepartmentName from Department')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response  # return the data as a JSON response

# this is a post route for adding a new user
@admins.route('/add_student', methods=['POST'])
def add_student():
    # get the data from the request
    studentAdd = request.form
    current_app.logger.info(studentAdd)  # log the data to the console
    cursor = db.get_db().cursor()  # get a cursor object from the database

    # get the data from the form
    FirstName = studentAdd['FirstName']
    LastName = studentAdd['LastName']
    StudentID = studentAdd['StudentID']
    Year = studentAdd['Year']
    Major = studentAdd['Major']
    Password = studentAdd['Password']

    # insert review data into the database
    query = f"""INSERT INTO Student (FirstName, LastName, StudentID, Year,  Major, Password)
    VALUES ('{FirstName}', '{LastName}', '{StudentID}', '{Year}', '{Major}', '{Password}')"""

    # query = f"""INSERT INTO Student (FirstName, LastName, StudentID, Year,  Major, Password)
    # VALUES ('Red', 'Foreman', '0000070', '5', 'Computer Science' , 'Angry')"""

    current_app.logger.info(query)
    cursor.execute(query)
    db.get_db().commit()
    return "Success! Review added"
