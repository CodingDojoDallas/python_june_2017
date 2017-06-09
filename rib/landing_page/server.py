from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)
    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')
def hello_world():
  return render_template('index.html')
    # Return the string 'Hello World!' as a response.
@app.route('/ninjas')
def ninjas():
  return render_template('ninjas.html')

@app.route('/dojos/new')
def dojo_new():
  return render_template('dojo_new.html')
                        							# function to the '/' route. This means that whenever we send a request to
                         					# localhost:5000/ we will run the following "hello_world" function.
app.run(debug=True)      					# Run the app in debug mode.