import sys
sys.path.insert(0, '/srv/www/pipeline/eus_pipeline')

import site
site.addsitedir('/srv/www/pipeline/eus_pipeline/.env/lib/python2.7/site-packages')

import settings

import django.core.management
django.core.management.setup_environ(settings)
utility = django.core.management.ManagementUtility()
command = utility.fetch_command('runserver')
command.validate()

import django.conf
import django.utils

django.utils.translation.activate(django.conf.settings.LANGUAGE_CODE)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
