
<h3 align="center">pythonservice</h3>

    
    <br />

This python service utilizes django and django rest framework to build a REST api service that can be accessed by different clients. It also employs Oauth2 using django-oauth-toolkit 
library for much a secure authentication protocol. Various unit tests and integration tests have been implemented to ensure the code implemented works as its suppost to. For CI/CD 
github actions was the choice as the workflows can be triggered on push or on creation of pull requests making sure everything works as its suppost to. The service also utilizes libraries like celery for ansychronous tasks in conjuction with a light weight database such as redis, in this case intergration with africa's talking sms api a celery task was created that handles sending of sms notification once an order has been created. 
The service has different environments i.e development environment which serves the purpose when the application is still in development utilizing its own resources required during the development stage, local environment for local development, production environment for production use cases. This environments help prevent much conflicts later on during the service development. 



<!-- GETTING STARTED -->

Clone Repository:
https://github.com/dom-inic/pythonservice.git
## Install and Run
```
Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python -m venv env
```
Activate the virtual environment

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```
Install all the project Requirements
```bash
pip install -r requirements.txt
```
-Apply migrations and create your superuser (follow the prompts)

```bash
# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser

Run the tests

```bash
# run django tests for main app
python manage.py test main
```


Run the development server

```bash
# run django development server
python manage.py runserver
``` 

open a new terminal window to launch celery
make sure you have redis installed on your machine

```bash
celery -A pythonservice worker -l info
``` 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



