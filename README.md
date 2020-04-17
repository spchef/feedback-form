# Python-Flask PostgreSQL 

Flask based feedback app buid in python , and results stored to postgres database .

Getting started
---------------

Download [Docker Desktop](https://www.docker.com/products/docker-desktop) for Mac or Windows. 
Enable Kubernetes from Preferences->Kubernetes-> Enable Kubernetes

Make sure you've installed kubectl binaries to talk to kubernetes API 
    * This is deployable to any kubernetes installation ( Verified with EKS and RKS )

Run the app in Kubernetes
-------------------------

Repo contains the yaml specifications to spin up flask as well as postgres microservices.

First create the feedback namespace

```
$ kubectl create namespace feedback
```

Run the following command to create the deployments and services objects:
```
$ kubectl apply -f postgres.yaml
service/postgres-svc created
persistentvolumeclaim/postgres-pv-claim created
deployment.extensions/postgres created
```
wait for the postgres service to start . 

```
$ kubectl create -f feedback-flask.yaml
service/feedback-service created
deployment.apps/feedback-flask created

```

The feedback page is then available over external Loadbalancer IP ,and the results are  available on port /results Endpoint.
```
kubectl get svc -n feedback
NAME               TYPE           CLUSTER-IP       EXTERNAL-IP                                                             PORT(S)        AGE
feedback-service   LoadBalancer   172.20.212.180   <EXTERNAL IP/LB>   80:32556/TCP   117s
postgres-svc       ClusterIP      172.20.194.193   <none>                                                                  5432/TCP       80s

```
## cleanup 

```
$ kubectl delete namespace feedback

```
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


