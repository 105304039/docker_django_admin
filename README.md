# docker_django_admin
## Description
Packing a Django 1.8.19 project where the Dockerfile helps download the related dependencies and set the password of superuser.


## Main Question
Solving the problem of setting the password of the superuser in the Dockerfile. The command `python3 manage.py createsuperuser --noinput` only receives username and email while the password cannot be customized. Note that the superuser can also be created when the docker container starts running and opened in terminal ([ref](https://stackoverflow.com/questions/18503770/how-to-create-user-from-django-shell)), but the question here focuses on solving this in the Dockerfile.

## Answer

### version constraints
One way of setting the superuser is using the package [django-createsuperuserwithpassword](https://pypi.org/project/django-createsuperuserwithpassword/), but the required framework of it is at least Django 1.11.

### My solution
At the CMD part, I create the superuser by using `python3 manage.py createsuperuser` and then use the changesuperuserpw.py to reset the password I want. The default username, password, and email are stored as ENV variables, so that I can overwrite them as I create the docker container.

```ruby
FROM python:3.7
EXPOSE 8000
WORKDIR /django_admin
COPY . .
ENV PASSWORD 000
ENV USERNAME abc
ENV EMAIL a@gmail.com
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE mysite.settings
RUN pip3 install -r requirements.txt --no-cache-dir
CMD python3 manage.py migrate; \
python3 manage.py createsuperuser --noinput --username $USERNAME --email $EMAIL; \
python3 changesuperuserpw.py -n $USERNAME -p $PASSWORD; \
python3 manage.py runserver 0.0.0.0:8000
```
<br>
Therefore, the command which builds the docker image is
```
docker run -it -p [port on your computer]:8000 \
    -e USERNAME=[your superuser name] \
    -e PASSWORD=[your superuser password] \
    -e EMAIL=[your superuser email] \
    [image_name] 
```
