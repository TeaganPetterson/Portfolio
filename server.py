from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from jinja2 import StrictUndefined
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    
	return render_template('index.html')

@app.route('/contact')
def contact_page():
      
	  return render_template('contact.html')

@app.route('/about')
def about_page():
      
	  return render_template('about.html')

@app.route('/experience')
def experience_page():

	return render_template('experience.html')

@app.route('/projects')
def projects_page():

	return render_template('projects.html')

@app.route('/work')
def work_page():

	return render_template('work.html')


if __name__ == "__main__":
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)