> django-admin startproject chaiaurDjango
cd chaiaurDjango

py manage.py runserver 5000

created views.py
from django.http import HttpResponse


def home(request):
    return HttpResponse ("Hello world")

def about(request):
    return HttpResponse ("Hello about")

def contact(request):
    return HttpResponse ("Hello contact")

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact "),
]

py manage.py runserver 8001

create templates : wrote basic code
creted static

views.py, modified and go back to settings.py > templates and modified > DIRS: 'templates'

runserver

setting.py 
line 12 > import os
line 120 >  STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")] //numbers might be vary cause of changes 😆

index.html > link css after title and line.1 


---------------------------------------
Jinja2 and django apps

install django extention in vscode
py manage.py startapp chai

settings.py > installed_app > "chai"
chai app > templates > chai> allchai.html

>>>>>>>>>>enable html django setting 
ctrl+, > emm > include language
item : djagno-html   value : html

created new urls.py in chai and make necessary settings in main project urls and mofified views in chai app

runserver
project main folder > templates > creating new file > layout.html
removed all project main index.html and wrote new with block code.

voila,,,,,

you can do same thing in app html. too,
simple comment down all the previous code or delete 
and paste and done

<!-- ------------------------------------------ -->
How to add tailwind in Django and super user

https://pypi.org/project/django-tailwind/

in case no have pip in system: python -m ensurepip --upgrade
                               python -m pip install
                               python -m pip install --upgrade

run this cmd : pip install django-tailwind
then run, : pip install 'django-tailwind[reload]'

main project settings.py > install new app> 'tailwind' and run cmd : py manage.py tailwind init> enter then add 'theme' app as well
after,
TAILWIND_APP_NAME = "theme"
INTERNAL_IPS= ['127.0.0.1'] line, 45,46

run cmd: py manage.py tailwind install
open cmd : run where npm
C:\Program Files\nodejs\npm.cmd
//getting error like not found npm/node.js even install so you add, this, NPM_BIN_PATH = r"C:/Program Files/nodejs/npm.cmd"
 to setings.py   ///line48
src: https://stackoverflow.com/questions/72033027/i-am-making-a-website-using-django-and-tailwind-css-but-in-cpanel-i-am-getting 

setting.py theme > base >tamplate>base.html copy > and adding to my templates. layout.html > '{% load static tailwind_tags %}'
same tilte unser css file too,

open new terminal > rename and change color , run: py manage.py tailwind start
switch to old terminal and reset run, py manage.py runserver 5000

not reloading and giving suggetions
project main > settings.py > intalled app> 'django_browser_reload',
                           > Middleware : 'django_browser_reload'.middleware.BrowserReloadMiddleware', 
            > urls> path("__reload__/", include('django_browser_reload.urls')),

runserver both....
voila 


time to move django admin pannel
py manage.py migrate
createsuper user and done... .
