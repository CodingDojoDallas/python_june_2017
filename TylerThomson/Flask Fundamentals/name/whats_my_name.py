from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def showName():
    print "This is my screen!"
    name = request.form['name']
    print name
    return redirect('/')

app.run(debug=True)