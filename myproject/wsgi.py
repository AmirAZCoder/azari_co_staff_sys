import os
from django.core.wsgi import get_wsgi_application

# نام پروژه خود را اینجا جایگزین staffportal کنید اگر متفاوت است
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'staffportal.settings')

application = get_wsgi_application()
