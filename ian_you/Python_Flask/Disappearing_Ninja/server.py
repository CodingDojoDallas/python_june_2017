from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def allninja():
    return render_template('allNinjas.html')

@app.route('/ninja/<color>')
def colorninja(color):
    if color == "blue" or color == "red" or color == "orange" or color == "purple":
        return render_template('ninja.html', color=color)
    else:
        color="notapril"
        return render_template('ninja.html', color=color)

app.run(debug=True)
