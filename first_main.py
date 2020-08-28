# This is Flask Rest Framework to create an RESTFull APIs/WebServices
import time
from flask import Flask,request
from flask_cors import cross_origin # This is nothing but CORS = Cross-Origin Resource Sharing to work with Web
from flask_restful import reqparse # flask_restful = Simple framework for creating REST APIs

app = Flask(__name__)

@app.route("/insert", methods = ["Post"]) # /insert : This is an Endpoint
@cross_origin()
def insert_func():
    parser = reqparse.RequestParser()  # Enables adding and parsing of multiple arguments in the context of a single request
    parser.add_argument('username', type=str)  # add_argument = Adds an argument to be parsed.
    args = parser.parse_args()  # Parse all arguments from the provided request and return the results as a Namespace
    username = str(args['username'])  # Assign the retrieved value to variable
    print("User name received : ", username)
    t = time.time()  # Current Time
    # Code to Insert Data into Database
    print("Total Time Taken : ", time.time() - t)
    return "Record inserted successfully"

@app.route("/view", methods = ["Get"]) # /view : This is an Endpoint
@cross_origin()
def view_func():
    parser = reqparse.RequestParser()  # Enables adding and parsing of multiple arguments in the context of a single request
    parser.add_argument('username', type=str)  # add_argument = Adds an argument to be parsed.
    args = parser.parse_args()  # Parse all arguments from the provided request and return the results as a Namespace
    username = str(args['username'])  # Assign the retrieved value to variable
    print("User name received : ", username)
    t = time.time()  # Current Time
    # Code to View the Data on the basis of entered input from Database
    print("Total Time Taken : ", time.time() - t)
    return "Record fetched successfully"

@app.route("/update", methods = ["Put"]) # /view : This is an Endpoint
@cross_origin()
def update_func():
    parser = reqparse.RequestParser()  # Enables adding and parsing of multiple arguments in the context of a single request
    parser.add_argument('username', type=str)  # add_argument = Adds an argument to be parsed.
    args = parser.parse_args()  # Parse all arguments from the provided request and return the results as a Namespace
    username = str(args['username'])  # Assign the retrieved value to variable
    print("User name received : ", username)
    t = time.time()  # Current Time
    # Code to Update the Data on the basis of entered input from Database
    print("Total Time Taken : ", time.time() - t)
    return "Record updated successfully"

@app.route("/delete", methods = ["Delete"]) # /delete : This is an Endpoint
@cross_origin()
def delete_func():
    parser = reqparse.RequestParser()  # Enables adding and parsing of multiple arguments in the context of a single request
    parser.add_argument('username', type=str)  # add_argument = Adds an argument to be parsed.
    args = parser.parse_args()  # Parse all arguments from the provided request and return the results as a Namespace
    username = str(args['username'])  # Assign the retrieved value to variable
    print("User name received : ", username)
    t = time.time()  # Current Time
    # Code to Delete the Data on the basis of entered input from Database
    print("Total Time Taken : ", time.time() - t)
    return "Record deleted successfully"

@app.route('/mix',methods=['POST','GET'])  # /mix : This is an Endpoint
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            # Code for POST method
            return "MIX POST Task done Successfully"
        except Exception as e:
            return print("Exception : ",e)
    if request.method == 'GET':
        try:
            # Code for GET method
            return "MIX GET Task done Successfully"
        except Exception as e:
            return print("Exception : ",e)

if __name__ == '__main__':
    app.run(debug=False)
    # app.run(host='0.0.0.0', port=8080, debug=True)
    # if you dont specify port it will take 5000 as default
    # if you dont specify host it will take 127.0.0.1 as default