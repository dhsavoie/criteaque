from flask import Blueprint, request, jsonify, make_response
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

# # Get all the admins from the database
# @admins.route('/admins', methods=['GET'])
# def get_admins():
#     # get a cursor object from the database
#     cursor = db.get_db().cursor()

#     # use cursor to query the database for a list of admins
#     cursor.execute('select adminCode, adminName, adminVendor from admins')

#     # grab the column headers from the returned data
#     column_headers = [x[0] for x in cursor.description]

#     # create an empty dictionary object to use in 
#     # putting column headers together with data
#     json_data = []

#     # fetch all the data from the cursor
#     theData = cursor.fetchall()

#     # for each of the rows, zip the data elements together with
#     # the column headers. 
#     for row in theData:
#         json_data.append(dict(zip(column_headers, row)))

#     return jsonify(json_data)
