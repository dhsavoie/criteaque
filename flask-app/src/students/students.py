from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


students = Blueprint('students', __name__)

# Get all students from the DB
@students.route('/students', methods=['GET'])
def get_students():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Student')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@students.route('/add_review', methods=['POST'])
def add_review():
    # will need to grab professor's id from their name as entered here
    review = request.form
    current_app.logger.info(review)
    cursor = db.get_db().cursor()
    ReviewContent = review['ReviewContent']
    Class = review['Class']
    WorkloadRating = review['WorkloadRating']
    DifficultyRating = review['DifficultyRating']
    EngagementRating = review['EngagementRating']
    StudentReviewer = review['StudentReviewer']
    ProfessorReviewed = review['ProfessorReviewed']
    prof_fname = ProfessorReviewed.split()[0]
    prof_lname = ProfessorReviewed.split()[1]
    cursor.execute('select ProfessorID from Professor where FirstName = %s and LastName = %s', (prof_fname, prof_lname))
    ProfessorID = cursor.fetchone()[0]
    query = f"""INSERT INTO Review (ReviewContent, Class, WorkloadRating, DifficultyRating, EngagementRating, StudentReviewer, 
    ProfessorReviewed) VALUES ('{ReviewContent}', '{Class}', {WorkloadRating}, {DifficultyRating}, {EngagementRating}, 
    {StudentReviewer}, '{ProfessorID}')"""
    current_app.logger.info(query)
    cursor.execute(query)
    db.get_db().commit()
    return "Success! Review added"

"""
# Get student detail for student with particular userID
@students.route('/students/<userID>', methods=['GET'])
def get_student(userID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from student where StudentID = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response"""