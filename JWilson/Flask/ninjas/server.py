from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "TestKey"
colors = ['red','orange','purple','blue']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    image = 'imgs/tmnt.png'
    return render_template('ninja.html',image=image)

@app.route('/ninjas/<color>')
def ninja(color):
    turtle = 'imgs/{}.jpg'.format(color)
    april = 'imgs/notapril.jpg'

    image = turtle if color in colors else april
   

    return render_template('ninja.html', image=image)

app.run(debug=True)