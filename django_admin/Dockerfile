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

