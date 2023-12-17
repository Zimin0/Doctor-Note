FROM python:3.9

COPY ./doctor-site /srv/www/doctor-site
COPY ./docker/python/create_migrations.sh /srv/www/doctor-site/create_migrations.sh
WORKDIR /srv/www/doctor-site

RUN chmod +x /srv/www/doctor-site/create_migrations.sh
RUN chmod +x /srv/www/doctor-site/create_superuser.py
RUN pip install -r requirements.txt
