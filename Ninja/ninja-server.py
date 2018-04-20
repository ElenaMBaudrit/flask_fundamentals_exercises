from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def allninjas():
    return render_template('ninjas.html')

@app.route('/ninjas/<color>')
def ninjaPick(color):
    selected=''
    if color=="purple":
        selected="donatello.jpg"
    elif color=="blue": 
        selected="leonardo.jpg"
    elif color=="orange": 
        selected="michelangelo.jpg"
    elif color=="red": 
        selected="raphael.jpg"
    else:
      selected="notapril.jpg"
    return render_template('allninjas.html', selected=selected)

app.run(debug=True)