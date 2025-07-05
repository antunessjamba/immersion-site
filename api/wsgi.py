"""
WSGI config for immersion_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'immersion_site.settings')

# Configuração padrão do WSGI
application = get_wsgi_application()

# Função handler para o Vercel
def handler(event, context):
    return application(event['path'], event)