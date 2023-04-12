# docker_django_admin
## Description
Packing a Django 1.8.19 project. The Dockerfile helps download the related dependencies and set the password of superuser when the docker image is built.


## Main Question
Solving the problem of setting the password of superuser as the docker image is built. Note that the superuser can also be created when the docker container starts running and opened in terminal [ref](https://stackoverflow.com/questions/18503770/how-to-create-user-from-django-shell), but the question here focuses on the stage of docker image.

## Answer

### version constraints
One way of setting the superuser is using the package [django-createsuperuserwithpassword](https://pypi.org/project/django-createsuperuserwithpassword/), but the required framework of it is at least Django 1.11.

### My solution
I write the RUN 

<code>
FROM --platform=$BUILDPLATFORM python:3.7-alpine AS builder
EXPOSE 8000
WORKDIR /django_admin
COPY . .
ENV PASSWORD 000
ENV USERNAME abc
ENV EMAIL opening0922@gmail.com
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE mysite.settings
RUN pip3 install -r requirements.txt --no-cache-dir
CMD python3 manage.py migrate; \
python3 manage.py createsuperuser --noinput --username $USERNAME --email $EMAIL; \
python3 changesuperuserpw.py -n $USERNAME -p $PASSWORD; \
python3 manage.py runserver 0.0.0.0:8000
</code>
