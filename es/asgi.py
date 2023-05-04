# ASGI describes a common interface between a Python web application and the web server.

# ASGI and WSGI are both specifications for
# building Python web applications and connecting them to a web server.
# ASGI (Asynchronous Server Gateway Interface) is an evolution of WSGI 
# that was designed to support asynchronous web servers and applications. 
# It provides an interface for handling HTTP and WebSocket requests in a non-blocking way, 
# which allows for better performance and scalability. 

#This is Pre-structured file by Django Framework

"""
ASGI config for es project.
It exposes the ASGI callable as a module-level variable named ``application``.

"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'es.settings')
application = get_asgi_application()
