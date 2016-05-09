# toolsapi App [![Build Status](https://travis-ci.org/ebar0n/SD-ToolsApi.svg)](https://travis-ci.org/ebar0n/SD-ToolsApi)

## Integrate sevices:

0. Github `code control` [Github Docs](https://developer.github.com/)
0. Toggl `time control` [Toggl Docs](https://github.com/toggl/toggl_api_docs/blob/master/toggl_api.md)
0. Trello `tasks control` [Trello Docs](https://developers.trello.com/)
0. Taiga `tasks control` [Taiga Docs](http://taigaio.github.io/taiga-doc/dist/api.html)
0. Quickbooks `Invoice control` [Intuit Docs](https://developer.intuit.com/docs)
0. Telegram `Communication control` [Telegram Docs](https://core.telegram.org/api)
0. Slack `Communication control` [Slack Docs](https://api.slack.com/)
0. Digital Ocean `Server deployment control` [Digitalocean Docs](https://developers.digitalocean.com/documentation/)

What you want is to create a repo on Github, use Trello or Taiga for project management, registering time with Toggl, check invoice with quickbooks, notify interactions slack and telegram, as a final point, a click for of the project deploy to digitalocean.

## Instructions for Use

### Install and configure docker
0. Install and configure Docker

    0. docker [Docker](https://www.docker.com)

    0. docker-machine [machine](https://docs.docker.com/machine/) and [install-virtualbox](https://www.virtualbox.org/wiki/Downloads) *optional in linux* 

    0. docker-compose [compose](https://docs.docker.com/compose/install/)

0. Set Var Environment

    * Copy to `env.example` into `django/toolsapi/settings/.env`
    * Edit values in `django/toolsapi/settings/.env`

### Run the project for development
0. Only in docker-machine

    0. Pre-Build

            docker-machine create --driver virtualbox --virtualbox-memory 1024 --virtualbox-cpu-count 2 toolsapi
            docker-machine start toolsapi
            eval "$(docker-machine env toolsapi)"
            docker-machine ip toolsapi
            192.168.99.100
            echo "192.168.99.100 dev.toolsapi.com" | sudo tee -a /etc/hosts > /dev/null

0. Not use docker-machine

        echo "127.0.0.1 dev.toolsapi.com" | sudo tee -a /etc/hosts > /dev/null

0. Enable cache for Dev

    0. Install

            docker pull ebar0n/proxy-cache

            docker run --name proxy-cache -d --restart=always \
                --publish 3128:3128 --publish 3141:3141 --publish 3142:3142 \
                --volume /data/proxy-cache/squid/:/var/spool/squid3 \
                --volume /data/proxy-cache/devpi:/var/.devpi/server \
                --volume /data/proxy-cache/aptcacherng:/var/cache/apt-cacher-ng \
                ebar0n/proxy-cache

    0. Using

            docker start proxy-cache

    0. Check cache container IP == "172.17.0.2"

            docker inspect proxy-cache | grep '"IPAddress":'

0. Build

        docker-compose build

0. Create migrations
    
        docker-compose up -d postgres
        docker-compose run --rm django python manage.py migrate

0. Create superuser (Execute command and follow the steps)
    
        docker-compose run --rm django python manage.py createsuperuser

0. Run Django Project
        
        docker-compose up -d 
        
0. Open project on browser
        
        http://dev.toolsapi.com:8000

### Run tests to style

0. Run tests isort

        docker-compose run --rm django isort -c -rc -df

0. Run tests flake8

        docker-compose run --rm django flake8

### Run tests to code

0. Activate the Python Debugger

        docker-compose run --rm django py.test --ds=toolsapi.settings.testing --pdb

0. Run all the tests

        docker-compose run --rm django py.test --ds=toolsapi.settings.testing

### Django Internationalization

0. Use
    
    0. Execute this command to runs over the entire source tree of the current directory and pulls out all strings marked for translation.
            
            docker-compose run --rm django python manage.py makemessages -l es
    
    0. Compiles .po files to .mo files for use with builtin gettext support.
            
            docker-compose run --rm django python manage.py compilemessages

### Run the project for Production

0. Build

        docker-compose -f docker-compose-production.yml build

0. Initialize
        
        docker-compose -f docker-compose-production.yml up -d postgres
        docker-compose -f docker-compose-production.yml run --rm django python manage.py migrate --noinput
        docker-compose -f docker-compose-production.yml run --rm django python manage.py createsuperuser
        docker-compose -f docker-compose-production.yml run --rm django python manage.py collectstatic --noinput

0. Run Django server

        docker-compose -f docker-compose-production.yml up -d

0. Visit [dev.toolsapi.com](http://dev.toolsapi.com/)
