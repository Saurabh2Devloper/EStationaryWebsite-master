#This is Pre-structured file by Django Framework

# ASGI and WSGI are both specifications for
# building Python web applications and connecting them to a web server.
# WSGI (Web Server Gateway Interface) is a specification for how web servers and Python web frameworks communicate with each other.
# It defines a standard interface for web servers to communicate with Python web applications.
#  WSGI servers receive incoming HTTP requests, pass them to the Python application,
# and then send the response back to the web server. 
# WSGI is the interface that is commonly used for Python web development with frameworks such as Django and Flask

"""
WSGI config for es project.
It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'es.settings')
application = get_wsgi_application()


