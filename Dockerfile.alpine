FROM alpine:latest
MAINTAINER Bill Shetti "billshetti@gmail.com"
WORKDIR /app
ADD . /app
ENV MYSQL_ID="db_app_user" 
ENV MYSQL_PASSWORD="BILL" 
ENV MYSQL_SERVER="fitcyclecustomers.cy4b7ufzt54x.us-west-2.rds.amazonaws.com"
 
RUN apk update && \
    apk add mysql mysql-client && \
    apk add py-pip && \
    apk add py-sqlalchemy && \
    apk add py-flask && \
    apk add py-mysqldb && \
    apk add py-requests
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "api_server.py"]
