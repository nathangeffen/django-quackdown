Steps to a fully working Django website
=======================================

#. django-admin startproject *myproject*
#. ./manage.py startapp *myapp1*
#. ./manage.py syncdb
#. Uncomment django.contrib.admin in settings.py
#. Uncomment admin docs in settings.py
#. Uncomment all admin related lines in urls.py of project.
#. ./manage syncdb
#. Uncomment the app url include line urls.py
#. Create a working view and url conf for app
#. Create a working model for app
#. ./manage syncdb
#. implement pubman
