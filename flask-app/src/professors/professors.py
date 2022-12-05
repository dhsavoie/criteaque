from flask import Blueprint, request, jsonify, make_response
import json
from src import db


professors = Blueprint('professors', __name__)

# this is a route for listing all of the departments
@professors.route('/departments', methods=['GET'])
def get_departments():
    cursor = db.get_db().cursor() # get a cursor object from the database
    cursor.execute('select DepartmentName from Department') # get all department names
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response # return the data as a JSON response

# this is a route for listing all of the professors in a department
@professors.route('/dept_profs', methods=['POST'])
def get_dept_profs():
    dept = request.form # get the data from the request
    cursor = db.get_db().cursor()
    dept_name = dept['DepartmentName'] # get the department name from the form
    # execute query to get all professors in the department
    cursor.execute('select FirstName, LastName from Professor where Department = %s', (dept_name))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# this is a route to get all the courses which a professor teaches
@professors.route('/prof_courses', methods=['POST'])
def get_prof_courses():
    prof = request.form # get the data from the request
    cursor = db.get_db().cursor()
    prof_fname = prof['Name'].split()[0]
    prof_lname = prof['Name'].split()[1]
    # get professor id from first and last name
    cursor.execute('select ProfessorID from Professor where FirstName = %s and LastName = %s', (prof_fname, prof_lname))
    ProfessorID = cursor.fetchone()[0]
    # execute query to get all courses taught by the professor
    cursor.execute('select CourseName, CourseSection from Course where Professor = %s', (ProfessorID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# this is a route to get the average ratings for each category for a professor in a specific course
@professors.route('/prof_ratings', methods=['POST'])
def get_prof_ratings():
    req_review = request.form
    cursor = db.get_db().cursor()
    prof_fname = req_review['Name'].split()[0]
    prof_lname = req_review['Name'].split()[1]
    # get professor id from first and last name
    cursor.execute('select ProfessorID from Professor where FirstName = %s and LastName = %s', (prof_fname, prof_lname))
    ProfessorID = cursor.fetchone()[0]
    course = req_review['Course']
    # execute query to get ratings from reviews for the professor
    cursor.execute(f"select AVG(WorkloadRating) as WL_Rating, AVG(DifficultyRating) as D_Rating, AVG(EngagementRating) as E_Rating from Review where ProfessorReviewed = {ProfessorID} and Class = '{course}'")
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# this is a route to get all the reviews for a professor in a specific course
@professors.route('/prof_reviews', methods=['POST'])
def get_prof_reviews():
    req_review = request.form
    cursor = db.get_db().cursor()
    prof_fname = req_review['Name'].split()[0]
    prof_lname = req_review['Name'].split()[1]
    # get professor id from first and last name
    cursor.execute('select ProfessorID from Professor where FirstName = %s and LastName = %s', (prof_fname, prof_lname))
    ProfessorID = cursor.fetchone()[0]
    course = req_review['Course']
    # execute query to get ratings from reviews for the professor
    cursor.execute(f"select DifficultyRating, EngagementRating, WorkloadRating, ReviewContent from Review where ProfessorReviewed = {ProfessorID} and Class = '{course}'")
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
