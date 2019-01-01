# api_server

Load into whatever directory.


Modify mysql.json file with the right password and server and username for the DB


Modify the line "with open('../mysql.json') as json_data:" to "with open('mysql.json') as json_data:"


Modify the last line "app.run(host='172.31.9.213', port=5000)" with the right IP address


to run  ./api_server.py 


# docker image build & run

git clone directory

If you want to run ALPINE LINUX:

cp Dockerfile.Alpine Dockerfile

docker build -t miniapi .

docker run -e MYSQL_ID='db_app_user' -e MYSQL_PASSWORD='VMware123!' -e MYSQL_SERVER='fitcyclecustomers.cy4b7ufzt54x.us-west-2.rds.amazonaws.com' -p 5000:5000 miniapi


REPLACE your values for each of the parameters in the -e. Three are needed

MYSQL_ID -> id of the user in mysql

MYSQL_PASSWORD -> password for the user

MYSQL_SERVER -> location of the mysql server (IP or url or name)

If you want to run ubuntu LINUX:
cp Dockerfile.standard Dockerfile
docker build -t workingapp .
docker run -p 5000:5000 workingapp




