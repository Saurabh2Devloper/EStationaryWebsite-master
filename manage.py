# server-app runner file by Django
# Django's command-line utility for administrative tasks

# Neccessory imports
import os
import sys

# Main Defination
def main():
    # Run administrative tasks.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'es.settings')
    # implicite Exception Handling by Django
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# start-point of execution
if __name__ == '__main__':
    main()
