FROM ubuntu:latest
MAINTAINER Bill Shetti "billshetti@gmail.com"
RUN apt-get update -y && \
    apt-get install -y mysql-client && \
    apt-get install -y python-pip && \
    pip install --upgrade pip && \
    apt-get install -y python-sqlalchemy
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install PyMySQL
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["api_server.py"]
