from flask import Flask, render_template, request, redirect
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'assignment_emailvalidation')
# an example of running a query

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def verify():
    username = request.form['email'].split('@')[0]

    domainLength = len(request.form['email'].split('@')[1].split('.'))

    i=0
    domain=""

    for i in range (0, domainLength-1):
        domain += request.form['email'].split('@')[1].split('.')[i]+"."

    extension = request.form['email'].split('@')[1].split('.')[domainLength-1]

    if username == "" or domain == "" or extension == "":
        error = "Email is not a valid email address"

        return render_template('index.html', error=error)

    query = "INSERT INTO emails (username, domain, extension, created_at, updated_at) VALUES (:username, :domain, :extension, NOW(), NOW())"

    data = {
        'username':username,
        'domain': domain,
        'extension':extension
    }

    mysql.query_db(query, data)
    return redirect ('/success')

@app.route('/success')
def success():
    query = "SELECT username, domain, extension, created_at FROM emails;"
    emails = mysql.query_db(query)

    return render_template('success.html', emails=emails)

app.run(debug=True)
