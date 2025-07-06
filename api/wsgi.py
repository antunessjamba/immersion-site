"""
WSGI config for immersion_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""


import os
from django.core.wsgi import get_wsgi_application
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'immersion_site.settings')

# Aplica migrações para criar tabelas no PostgreSQL
django.setup()
from django.core.management import call_command
#call_command('migrate', '--noinput')

application = get_wsgi_application()
app = application  # Ponto de entrada para o Vercel