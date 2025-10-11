from django.core.wsgi import get_wsgi_application

import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "where_to_go.settings")

application = get_wsgi_application()
