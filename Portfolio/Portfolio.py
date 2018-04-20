from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')          
def portfolio_flask():
  return render_template('Portfolio-flask.html') 
  
@app.route('/Portfolio_Web')          
def Portfolio_Web():
  return render_template('Portfolio_Web.html')  
   
@app.route('/Portfolio_About')          
def Portfolio_About():
  return render_template('Portfolio_About.html') 
app.run(debug=True) 