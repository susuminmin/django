"""
WSGI config for django_intro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_intro.settings')

application = get_wsgi_application()

# Web Server Gateway Interface
# 사용자들이 실제 사용할 수 있도록 구축할 때 다시볼 것 
# 웹서비스로 배포할 때 필요한 파일 (추후 설명 ... ) 
