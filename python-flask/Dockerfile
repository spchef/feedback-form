FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN apk update && \
    apk add --virtual build-deps gcc musl-dev && \
    apk add postgresql-dev
RUN apk add bash
RUN pip install -r requirements.txt 
EXPOSE 5000 
#ENTRYPOINT [ "python" ] 
#CMD [ "app.py" ] 

