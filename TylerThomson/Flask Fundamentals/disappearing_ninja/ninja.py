from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninjas.html')

@app.route('/ninja/<color>')
def ninjas(color):
    if color.lower() in ['red', 'blue', 'purple', 'orange']:
        image = color + '.jpg'
    else:
        image = 'notapril.jpg'
    return render_template('ninja.html', image=image)
app.run(debug=True)
