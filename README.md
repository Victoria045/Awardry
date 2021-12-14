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

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the application | On application load | Display of Landing page |
| Create account by Sign Up | Enter email, username and password| Redirect to login|
| Login selected | Enter username and password you signed up with| Redirect to home page|
| Submit website button selected | Submit | Input details in a form and upload |
| Click on the image | CLick | Redirected to page with image details and rate on them |
| Click the user profile icon | Select Profile | Redirected to profile page where you can edit profile |
| Click the user profile icon | Select Edit Profile | A form displays where you can edit profile |
| Click the user profile icon | Select Logout | Logout and redirected to login page |

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