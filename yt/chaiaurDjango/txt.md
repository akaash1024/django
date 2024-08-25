> django-admin startproject chaiaurDjango
cd chaiaurDjango

py manage.py runserver 5000

created views.py in main project chaiaurDjango    <<<<<<<<<<<<<
from django.http import HttpResponse


def home(request):
    return HttpResponse ("Hello world")

def about(request):
    return HttpResponse ("Hello about")

def contact(request):
    return HttpResponse ("Hello contact")

urls.py in main project chaiaurDjango             <<<<<<<<<<<<
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
in main project chaiaurdjago
create templates > website > index.html : wrote basic code
creted static folder and make styles.css

in main project views.py                                
commment HttpResponse and render request with template urls then go back to  
settings.py > templates and modified > DIRS: 'templates'         
views.py, modified and go back to settings.py > templates and modified > DIRS: 'templates'

runserver

setting.py 
line 12 > import os
line 129 >  STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

index.html > link css after title '<link rel="stylesheet" href="{% static 'style.css' %}">'
and line.2 '{% load static %}'      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

TILL now we had worked on project only time to work on app >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



---------------------------------------
Jinja2 and django apps


install django extention in vscode         >>>>>>>>>>>>>>>>> this is extention for better suggestion and fast writing
py manage.py startapp chai

settings.py > installed_app > "chai"
chai app > templates > chai> allchai.html  >>>>>>>>>>>>>added boiler row code

>>>>>>>>>>enable html django setting 
ctrl+, > emm > include language
item : djagno-html   value : html

created new file "urls.py" in chai 
and make necessary changes in main project urls.py and mofified views in chai app  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

runserver
project main folder > templates > creating new file > layout.html
removed all boiler code html code from project main index.html and wrote new with block code.

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


/////////////
RESET pass django
py manage.py changepassword

making models in chai
 pip install Pillow

main project chaiaruDjango
> settings.py > 
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
> urls.py >
    from django.conf import settings
    from django.conf.urls.static import static
    then add,+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

now,
python manage.py makemigrations chai
python manage.py migrate

> admin and register for admin view.. .
    from django.contrib import admin
    from .models import ChaiVariety

    admin.site.register(ChaiVariety)

- In Python, the double underscore (__) is often referred to as a "dunder".
                                    <> //this is called dimond bracket

in chai views editing, in all_chai defination 
    chais = models.ChaiVariety.objects.all()
    return render(request, "chai/allChai.html", {'chais':chais}) //dd 
and add loop in allChai.html  //add url for handling image smoothly
added new description field in models> makemigration and migrate too,

moving to the next part id n all... .
creting new view for details > chai_details

            NOTE - this is {{}} variable // this is {% %}
linked allchai.html, urls and details.html > facing image issue in detail.html

Voila fixed

