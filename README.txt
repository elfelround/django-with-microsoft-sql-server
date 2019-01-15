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





