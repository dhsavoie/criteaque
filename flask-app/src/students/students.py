from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


students = Blueprint('students', __name__)

# this is a post route for adding a new review
@students.route('/add_review', methods=['POST'])
def add_review():
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

    # get the professor's ID from their name
    prof_fname = ProfessorReviewed.split()[0]
    prof_lname = ProfessorReviewed.split()[1]
    cursor.execute('select ProfessorID from Professor where FirstName = %s and LastName = %s', (prof_fname, prof_lname))
    ProfessorID = cursor.fetchone()[0]

    # insert review data into the database
    query = f"""INSERT INTO Review (ReviewContent, Class, WorkloadRating, DifficultyRating, EngagementRating, StudentReviewer, 
    ProfessorReviewed) VALUES ('{ReviewContent}', '{Class}', {WorkloadRating}, {DifficultyRating}, {EngagementRating}, 
    {StudentReviewer}, {ProfessorID})"""
    current_app.logger.info(query)
    cursor.execute(query)
    db.get_db().commit()
    return "Success! Review added"