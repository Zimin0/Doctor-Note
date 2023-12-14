from multiprocessing import cpu_count
from os import environ

def get_workers():
    return cpu_count()

bind = '0.0.0.0:' + environ.get('PORT', '8000')
max_requests = 1000
worker_class = 'gevent'
workers = get_workers()

env = {
    'DJANGO_SETTINGS_MODULE': 'config.settings'
}

reload = True

name = 'doctor-site'