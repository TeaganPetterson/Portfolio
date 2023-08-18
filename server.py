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

@app.route('/contact_page')
def contact_page():
      
	  return render_template('contact.html')

@app.route('/experience_page')
def experience_page():

	return render_template('experience.html')

@app.route('/projects_page')
def projects_page():

	return render_template('projects.html')


if __name__ == "__main__":
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)