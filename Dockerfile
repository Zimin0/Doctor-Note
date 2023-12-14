FROM python3:9

COPY ./ /srv/www/doctor-site
WORKDIR /srv/www/doctor-site

RUN pip install -r requirements.txt
