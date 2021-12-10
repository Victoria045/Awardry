# Awardry

## Author 
Built by: [Victoria Beryl](https://github.com/Victoria045)

# Description
Awardry is a Django application that enables users to showcase their projects to which they can be rated in terms of the design,usability and content by other users. 

#### Prerequisites 
* python3.6
* pip
* Django

## User Story
* View posted projects and their details.
* Post projects to be rated/reviewed.
* Rate/Review other user's projects.
* Search for projects.
* View projects overal score.
* View profile page.

# Setup and Installation
#### Cloning the repository
* Open Terminal:
```bash
        $ git clone https://github.com/Victoria045/Awardry.git
        $ cd Awardry
        $ code . or atom . based on your text editor 
```
* Navigate into the folder, install and activate virtual environment
```bash
      $ python -m venv virtual

      $ source virtual/bin/acivate
```
* Install all dependencies in requirements.txt
```bash
      $ pip install -r requirements.txt
```
#### Setup the Database
* Setup the database username, password, host then make migrations  
```bash
      $ python manage.py makemigrations 
```
* Run migrations
```bash
      $ python manage.py migrate
```
### Running the Application
* To run the application, open the cloned repo in terminal and run the following commands:
```bash
      $ python3 manage.py runserver
```
### Testing the Application       
* To run unittests for the class application and check if it functions well:
```bash
      $ python3 manage.py test award
```
## Known Bugs
* No known bugs so far, incase a bug is spotted pull requests are allowed.


## Technologies Used
* markdown

* Django_Bootstrap4 - for bootstrap version 4

* Heroku - online deployment


## Support and contact details
Incase of any issues at hand, please email me at victoriaberyl45@gmail.com

### License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/Victoria045/Awardry/blob/master/LICENSE) 