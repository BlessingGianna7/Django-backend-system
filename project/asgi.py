
import os
from django.core.asgi import get_asgi_application
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi_app import app as fastapi_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wildlife_conservation.settings')
django_app = get_asgi_application()


application = fastapi_app
