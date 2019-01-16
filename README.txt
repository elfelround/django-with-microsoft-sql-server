install docker to dockerize microsoft's software, remember to spring holy water all over before
going microsoft
https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1

add repository update and
$ sudo apt-get install docker-ce

///
install docker compose
https://docs.docker.com/compose/install/

$sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

$sudo chmod +x /usr/local/bin/docker-compose

$ docker-compose --version
///


download docker image (aka docker pull)
$ sudo docker pull microsoft/mssql-server-linux
por el momento funciona pero se supone ke lo mueven todo a cacasoft servers

since cookiecutter will link us a postgres and could ask to use docker will focus on an normal django installation

$ docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=yourStrong(!)Password' -p 1433:1433 -d microsoft/mssql-server-linux

cd docker_config && sudo docker-compose up -d
//since i had already installed the docker and stopped it manually the output was shorter than usual but still created stuff to db

sudo docker exec -i -t <id de la db e64abc3a8b65> /bin/bash
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa

StrongPass123
CREATE DATABASE django_mssql_test;
go
SELECT Name from sys.Databases;            //making interrogations(querying) inside mssql
go
Name

install  FreeTDS, it was a pain in the a$$ and i had to touch a lot of /etc/ dirs with sudo priviledges

can check if its installed afterwards by
tsql -C

sudo apt-get install unixodbc-dev
pip3 install django-pyodbc-azure==2.0.4.1
pip3 install pyodbc==4.0.23      //installed 25 at time of running this, i installed this on global not on shell since the text script had to find some local path

i had an error where there wasnt libtsodbc.so at running test so i had to sudo apt-get install freetds-dev
sudo apt-get install tdsodbc
python3 test.py (decided to place it at home)

now time to install the dependencies on the environment

(changed settings)
pipenv shell 
python3 manage.py migrate
//applied migrations


Docker technology and the package django-pyodbc-azure, you will be able to connect your Django application to MSSQL database locally using the latest version of Ubuntu (Ubuntu 18), even though MSSQL is not officially supported yet


