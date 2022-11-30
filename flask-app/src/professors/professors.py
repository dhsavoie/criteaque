from flask import Blueprint, request, jsonify, make_response
import json
from src import db


professors = Blueprint('professors', __name__)

# Get all the professors from the database
@professors.route('/professors', methods=['GET'])
def get_professors():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of professors
    cursor.execute('select professorCode, professorName, professorVendor from professors')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the top 5 professors from the database
@professors.route('/top5professors')
def get_most_pop_professors():
    cursor = db.get_db().cursor()
    query = '''
        SELECT p.professorCode, professorName, sum(quantityOrdered) as totalOrders
        FROM professors p JOIN orderdetails od on p.professorCode = od.professorCode
        GROUP BY p.professorCode, professorName
        ORDER BY totalOrders DESC
        LIMIT 5;
    '''
    cursor.execute(query)
       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)