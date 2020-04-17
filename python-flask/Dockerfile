FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN apk update && \
    apk add  --no-cache --virtual build-deps gcc musl-dev && \
    apk add --no-cache postgresql-dev
RUN pip install -r requirements.txt 
EXPOSE 80 
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 

