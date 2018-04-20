from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("MyName.html")

@app.route('/process', methods=['POST'])
def create_user():
    name = request.form['name']
    print name
    return redirect('/')
app.run(debug=True)


'''
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   email = request.form['email']
   # redirects back to the '/' route
   return redirect('/')
app.run(debug=Truecopy) # run our ser
'''