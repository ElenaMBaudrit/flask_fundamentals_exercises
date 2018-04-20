from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("DojoSurvey.html")

@app.route('/user', methods=['POST'])
def create_user():
    print "Got Post Info"
    return render_template('/user.html', name=request.form['name'], location=request.form['location'], language=request.form['language'], comments=request.form['comments'])

@app.route('/')
def index():
    return render_template("DojoSurvey.html")

app.run(debug=True)




'''
@app.route('/user')
def create_user(search):
    results = []
    search_string = search.data['search']
 
    if search.data['search'] == '':
        qry = db_session.query(Album)
        results = qry.all()
 
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', table=table)

app.run(debug=True)
'''