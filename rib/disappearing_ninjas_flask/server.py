from flask import Flask, render_template, request, url_for	# Import Flask to allow us to create our app.
app = Flask(__name__)										# Global variable __name__ tells Flask whether or not we are running the file
															# directly, or importing it as a module.
@app.route('/')
def index():
	return render_template('index.html')
															# Return the string 'Hello World!' as a response.
 
@app.route('/ninja')									# The "@" symbol designates a "decorator" which attaches the following
def show_ninja():
	return render_template('ninja.html')
    
@app.route('/ninja/<color>')
def ninja(color):
    if color.lower() in ['red', 'blue', 'purple', 'orange']:
        image = color + '.jpg'
    else:
        image = 'notapril.jpg'
    
    return render_template('blue.html', image=image)


app.run(debug=True)