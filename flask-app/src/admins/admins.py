from flask import Blueprint, request, jsonify, make_response
import json
from src import db


admins = Blueprint('admins', __name__)

# Get all the admins from the database
@admins.route('/admins', methods=['GET'])
def get_admins():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of admins
    cursor.execute('select adminCode, adminName, adminVendor from admins')

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

# get the top 5 admins from the database
@admins.route('/top5admins')
def get_most_pop_admins():
    cursor = db.get_db().cursor()
    query = '''
        SELECT p.adminCode, adminName, sum(quantityOrdered) as totalOrders
        FROM admins p JOIN orderdetails od on p.adminCode = od.adminCode
        GROUP BY p.adminCode, adminName
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