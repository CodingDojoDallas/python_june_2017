from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

# @app.route('/friends/<friend_id>')
# def show(friend_id):
# 	#Write a query to select specific user by id. At tevey point where
# 	#we want to insert data, we write ':' and variable name.
# 	query = 'SELECT * FROM friends WHERE id= :specifc_id'
# 	#Then define a dictionary with key that matches :variable_name in query.
# 	data = {'specific_id': friend_id}
# 	#Run query with inserted data
# 	friends = mysql.query_db(query, data)
# 	#Friends should be a list with a single object,
# 	#so we pass the value at [0] to our template under alias one_friend
# 	return render_template('index.html', one_friend= friends[0])

@app.route('/')
def index():
	return render_template('index.html')
	query = 'SEECT * FROM friends'	#defines my query
	friends = mysql.query_db('SELECT * FROM friends')	#runs query_db()
	print friends
	return render_template('index.html', all_friends=friends)	#pass data to our template


@app.route('/friends', methods=['POST'])
def create():
	# add a friend to the database!
	query = 'INSERT NTO friends(first_name, last_name, occupation created_at, updated_at)VALUES(first_name,last_name,:occupation, NOW(),NOW())'
	
	data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
	}
	print request.form['first_name']
	print request.form['last_name']
	print request.form['occupation']
	mySQL.query_db(query, data)
	return redirect('/')

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
	query = "DELETE FROM friends WHERE id = :id"
	data = {'id': friend_id}
	mysql.query_db(query, data)
	return redirect('/')
app.run(debug=True)