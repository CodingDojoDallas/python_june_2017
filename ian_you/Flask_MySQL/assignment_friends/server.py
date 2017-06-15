from flask import Flask, render_template, request, redirect
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'assignment_friends')
# an example of running a query

@app.route('/')
def index():
    query = "SELECT * FROM friends;"
    friends = mysql.query_db(query)
    return render_template('index.html', friends=friends)


@app.route('/add', methods = ['POST'])
def add():
    query = "INSERT INTO friends (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW());"

    data = {
        'name':request.form['name'],
        'age':request.form['age'],
    }
    mysql.query_db(query, data)
    return redirect ('/')

app.run(debug=True)
