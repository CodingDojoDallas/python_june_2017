from flask import Flask, render_template,session,redirect
app = Flask(__name__)
app.secret_key = "Welp"

def count():
    session['count'] = 0

@app.route('/')
def index():
    session['count'] += 1
    return render_template('index.html',count=session['count'])

@app.route('/twice')
def twice():
    session['count'] +=1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)
 