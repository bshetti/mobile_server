FROM alpine:latest
MAINTAINER Bill Shetti "billshetti@gmail.com"
WORKDIR /app
ADD . /app
ENV FITCYCLEAPI="privileged-cluster-3-bfa45254-9c2d-11e8-9f9e-060011e8e588.9e425f07-d492-417d-97c6-867e83efa076.cascade-domain.com:30431/api/v1.0/signups" 
 
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
CMD ["python", "mobile_server.py"]
