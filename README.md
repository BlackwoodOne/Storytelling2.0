# Storytelling 2.0

This game was developed as a part of the "Computer Supported Cooperative Work and Social Computing" lecture at University Hamburg.
The project is not feature complete, but feel free to play or develop!
 
Team:
@BlackwoodOne
@kamila3107
@Toastgeraet
@then4p

## Installation

### Windows
Anaconda with Python 3.6

*Package requirements in Conda Env:*  
* django  
* mysqlclient
* mysql-connector
* connector-c  

*Through pip:*  
* django-bootstrap4  
* channels  
* msgpack  

*Command:*  
    
    pip install django-bootstrap4 channels msgpack

### Django Channels

- Install Docker
- Run Redis Image (is downloaded automatically)  

        docker run -p 6379:6379 -d redis:2.8

- Install Django Channels-Redis Interface  

        pip install channels_redis

### Requirement MySQL Server needed:  

#### Windows  
* MySql Server with legacy Authentication Support  
* leave the root password blank  
* Recommend MySQL Workbench as interface  
* create a Schema called 'cscw'  

Then run the commands below in an active anaconda env.

### Initialize and run
Start Django Dev Server with Anaconda Env Shell  

    cd PROJECT_DIRECTORY

    python manage.py migrate
    python manage.py loaddata initializeDefFields.json
    python manage.py runserver



