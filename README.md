# Python-Flask PostgreSQL 

App to display a feedback form using Python Flask, store the entered data in a PostgreSQL database 

Getting started
---------------

Download [Docker Desktop](https://www.docker.com/products/docker-desktop) for Mac or Windows. 
Enable Kubernetes from Preferences->Kubernetes-> Enable Kubernetes

Make sure you've installed kubectl binaries to talk to kubernetes API 

Run the app in Kubernetes
-------------------------

Repo contains the yaml specifications to spin up flask as well as postgres microservices.

First create the feedback namespace

```
$ kubectl create namespace vote
```

Run the following command to create the deployments and services objects:
```
$ kubectl create -f k8s-specifications/
deployment "db" created
service "db" created
deployment "redis" created
service "redis" created
deployment "result" created
service "result" created
deployment "vote" created
service "vote" created
deployment "worker" created
```

The vote interface is then available on port 31000 on each host of the cluster, the result one is available on port 31001.




## Setup on local

* Create PostgreSQL database and add access credential `SQLALCHEMY_DATABASE_URI` to your own config.py file (Will be removed from repo soon*)
* Create mailtrap.io account and add access credentials `MAIL_LOGIN` and `MAIL_PASSWORD` to your own config.py file (not in repo)
* Run `pipenv shell` then `pipenv install` to install dependencies
* Run `python app.py` to open app in server `localhost: 80`



## Status & To-do list

* Status: Fully working in dev. Deployable to K8s

* To-do: Use to create more advanced Python-PostgreSQL app 
*        Sendmail script need to be fixed ,Plan to use GMAIL SMTP 
*        Secret and configmaps need to be used to handle DB connection and HTTP auth 
*        config.py to read from env using os module in python


