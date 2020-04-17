# Python-Flask PostgreSQL Heroku

App to display a feedback form using Python Flask, store the entered data in a PostgreSQL database 

## Setup

* Create PostgreSQL database and add access credential `SQLALCHEMY_DATABASE_URI` to your own config.py file (not in repo)
* Create mailtrap.io account and add access credentials `MAIL_LOGIN` and `MAIL_PASSWORD` to your own config.py file (not in repo)
* Run `pipenv shell` then `pipenv install` to install dependencies
* Run `python app.py` to open app in server `localhost: 5000`

## Code Examples

* code to submit completed form tto Postgres database

```python
@app.route('/submit', methods=['POST'])
def submit():
  if request.method == 'POST':
    customer = request.form['customer']
    dealer = request.form['dealer']
    rating = request.form['rating']
    comments = request.form['comments']
    if customer == '' or dealer == '':
      return render_template('index.html', message='Please enter required fields')
    if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
      data = Feedback(customer, dealer, rating, comments)
      db.session.add(data)
      db.session.commit()
      send_mail(customer, dealer, rating, comments)
      return render_template('success.html')
    return render_template('index.html', message='You have already submitted feedback')
```

## Status & To-do list

* Status: Fully working in dev. Deployed to K8s

* To-do: Use to create more advanced Python-PostgreSQL app


