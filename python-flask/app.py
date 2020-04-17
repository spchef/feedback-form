from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

import config

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
  app.debug = True
  app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

else:
  app.debug = False
  app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
  __tablename__ = 'feedback'
  id = db.Column(db.Integer, primary_key=True)
  attendee = db.Column(db.String(200), unique=True)
  rating = db.Column(db.Integer)
  comments = db.Column(db.Text())

  def __init__(self, attendee, rating, comments):
    self.attendee = attendee
    self.rating = rating
    self.comments = comments

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
  if request.method == 'POST':
    attendee = request.form['attendee']
    rating = request.form['rating']
    comments = request.form['comments']
    if attendee == '' :
      return render_template('index.html', message='Please enter required fields')
    if db.session.query(Feedback).filter(Feedback.attendee == attendee).count() == 0 :
      data = Feedback(attendee, rating, comments)
      db.session.add(data)
      db.session.commit()
      #send_mail(attendee, rating, comments)
      return render_template('success.html')
    return render_template('index.html', message='You have already submitted feedback')

auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

@app.route('/results', methods=['GET'])

@auth.login_required
def results():
  if request.method == 'GET':
    feedback=Feedback.query.all()
    
    return render_template ('results.html' ,feedback=feedback)

if __name__ == '__main__':
  db.create_all()
  app.debug = True
  app.run(host='0.0.0.0',port=80)
