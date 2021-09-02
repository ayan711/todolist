import MySQLdb
from flask import Flask, render_template, request, jsonify
import requests
from flask_mysqldb import MySQL
from flask_cors import CORS
import os,time


app = Flask(__name__) 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass,123'
app.config['MYSQL_DB'] = 'to_do'
# app.run(debug=True)
mysql = MySQL(app)

# @app.route("/")
# def index():
#    return "WELCOME!!! This is the home page"

@app.route('/insert')
def insertActivity():

    activity_ID = request.args.get("activity_ID")
    activity = request.args.get("activity")
    activity_desc = request.args.get("activity_desc")

    cur = mysql.connection.cursor()


    query_addActivity="INSERT INTO user_activity VALUES (%s,%s,%s)" # WHERE State like %s AND County like %s "
    cur.execute(query_addActivity,(activity_ID,activity,activity_desc) )

    mysql.connection.commit()


    print('Added entry')

    return "Added entry"


# @app.route('/')
# def insertActivity():

#     # activity_ID = request.args.get("activity_ID")
#     # activity = request.args.get("activity")
#     # activity_desc = request.args.get("activity_desc")

#     cur = mysql.connection.cursor()

#     query_addActivity="INSERT INTO user_activity VALUES (2,'test','test')"
#     cur.execute(query_addActivity)
#     # query_addActivity="INSERT INTO user_activity VALUES (%s,%s,%s)" # WHERE State like %s AND County like %s "
#     # cur.execute(query_addActivity,(activity_ID,activity,activity_desc) )

#     mysql.connection.commit()


#     print('Added entry')

#     return "Added entry"


if __name__ == '__main__':
    #app.run()
    app.run(host="127.0.0.1", port=5000)