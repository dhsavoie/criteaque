from flask import Blueprint, request, jsonify, make_response
import json
from src import db


students = Blueprint('students', __name__)

# Get all students from the DB
@students.route('/students', methods=['GET'])
def get_students():
    cursor.execute('select studentNumber, studentName,\
        creditLimit from students')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get student detail for student with particular userID
@students.route('/students/<userID>', methods=['GET'])
def get_student(userID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from students where studentNumber = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response