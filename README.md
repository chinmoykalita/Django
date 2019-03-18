# Project Title
~~~
Personal gallery application 
~~~
### Getting Started
~~~
~~~
### Prerequisites
~~~
.Install UBUNTU OS
.Install Visual studio code.
~~~
###  Installing
~~~
.Install Django framework
.Install boostrap
.I nstall psycopg2 to connect Django with Database
~~~
### Running the tests
~~~
.Tests are in tests.py fife

.Make virtual active
.Run python3.6 manage.py test photos in terminal
~~~
### Break down into end to end tests
~~~
.test for creating ,image,category,location instances
.test for saving image,category,location
.test for deleting image
.test for updating image
.test for displaying image
~~~
### Deployment
~~~
Step 1. Create a Procfile in my project root.

Step 2. Do this in my app/settings.py

   app/settings.py

    import django_heroku 
    # Then all the way at the bottom of the file
 
    django_heroku.settings(locals())
Step 3. Then do this in your command line (bash).

pip install gunicorn
pip install django-heroku
pip freeze > requirements.txt
# login to your heroku
heroku login
# create new app if one doesn't yet exist
heroku create
# create a new postgres database for your app
heroku addons:create heroku-postgresql:hobby-dev
# migrate your database to the heroku app
heroku run python manage.py migrate
# before you do this, make sure to add your SECRET_KEY to your env variables in your heroku app settings
git add .
git commit -m "Ready to heroku this sucker in the face."
git push heroku master