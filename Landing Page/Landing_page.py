from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/Ninjas', methods=['GET'])
def Ninjas():
   print "Ninjas information"
   return render_template("Ninjas.html")

@app.route('/dojos', methods=['GET']) #https://airbrake.io/blog/http-errors/405-method-not-allowed
def dojos():
  print "Dojos"
  return render_template("dojos.html")
app.run(debug=True) 

@app.route('/', methods=['GET'])
def index1():
   print "Index"
   return render_template("index.html")




