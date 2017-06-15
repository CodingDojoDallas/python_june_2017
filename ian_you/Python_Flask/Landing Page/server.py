from flask import Flask, render_template

app= Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", word="Home Page")
@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html", word="Ninjas")
@app.route('/dojos/new')
def dojo():
    return render_template("dojos.html", word="Ninjas")
app.run(debug=True)
