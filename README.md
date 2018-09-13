#data uploader
IF YOU WANT TO CLONE HERES THE QUICKSTART RUNNING LOCALLY: git clone https://github.com/djangorobert/datauploader.git

cd datauploader

python manage.py migrate python manage.py runserver

http://localhost:8000/polls/
#Login Page
![Alt text](datauploadz.JPG?raw=true)


#Upload File page

![Alt text](uploadsnip.JPG?raw=true)

#Uploaded Files

![Alt text](uploadlists.JPG?raw=true)


#Steps to recreate project.

#Create a virtualenviorment 
virtualenv yourenviormentnamehere
cd yourenviormentnamehere

#activate virtualenviorment for Windows 
.\scripts\activate

#Use PIP to install python packages
pip install django
#This will install django 

#Next create  a project
django-admin startproject nameyourprojecthere

#cd into the project
cd nameyourprojecthere

#run your migrations
python manage.py makemigrations
python manage.py migrate

#create a superuser for the django free admin
python manage.py createsuperuser

#sanity check to see if its working on your local machine.
python manage.py runserver


#go to localhost:8000
you should see a working page.

#Create a APP with Django
python manage.py startapp yourappsnamehere

#after its created go to settings.py add the app INSTALLED APPS like this 'app',

#Create your django Model a model is like the blueprint it is the logic of your app
In this app were creating a Model called Submission and it will have fields like: you, filename, description, timestamp, audience.

this will be the data that the User will be uploading in the User Interface before they submit us the data.


#Next you will do the Views this is were the rendering of data happens 
We used class based views for this project.
#EXAMPLE of the Upload view
class UploadFileView(CreateView):
    form_class = SubmissionForm
    success_url = reverse_lazy('submitted')
    template_name = 'datauploader/upload.html'

#the Templates is what the user will see 
Django uses the Jina template language to make it simple as well
here is a example of our upload.html


{% extends 'datauploader/base.html' %}


{% block content %}

    <h1>Upload file</h1>
    <form method="POST" class="post-form" enctype="multipart/form-data">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-warning">post</button>
    </form>
{% endblock %}

Thats it the rest of the code is here on github. thanks.

