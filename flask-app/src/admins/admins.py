from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


admins = Blueprint('admins', __name__)

# this is a route for listing all of the departments
@admins.route('/get_majors', methods=['GET'])
def get_majors():
    cursor = db.get_db().cursor() # get a cursor object from the database
    cursor.execute('select Major from Major') # get all department names
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response # return the data as a JSON response

    # this is a post route for adding a new user
@admins.route('/add_student', methods=['POST'])
def add_student():
    # get the data from the request
    review = request.form
    current_app.logger.info(review) # log the data to the console
    cursor = db.get_db().cursor() # get a cursor object from the database

    # get the data from the form
    ReviewContent = review['ReviewContent']
    Class = review['Class']
    WorkloadRating = review['WorkloadRating']
    DifficultyRating = review['DifficultyRating']
    EngagementRating = review['EngagementRating']
    StudentReviewer = review['StudentReviewer']
    ProfessorReviewed = review['ProfessorReviewed']

    # insert review data into the database
    query = f"""INSERT INTO Review (ReviewContent, Class, WorkloadRating, DifficultyRating, EngagementRating, StudentReviewer, 
    ProfessorReviewed) VALUES ('{ReviewContent}', '{Class}', {WorkloadRating}, {DifficultyRating}, {EngagementRating}, 
    {StudentReviewer}, {ProfessorID})"""
    current_app.logger.info(query)
    cursor.execute(query)
    db.get_db().commit()
    return "Success! Review added"