dashboard
=========

The (django?) server that controls the global state of the system, serves 
a dashboard page on the master server, and handles real-time audience
input / feedback. 

How to get started

create a virtual env,
activate it
pip install requirements.txt
install mysql on your comp if you haven't
create a user with username root and password NONE
sql> create database dashboard;
python manage.py syncdb
python manage.py migrate voting
python manage.py runserver
