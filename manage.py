#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_empresas.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

    # Entornos virtuales
    .venv /
    venv /
    env /

    # Archivos temporales de Python
    __pycache__ /
    *.py[cod]

    # Configuración local de PyCharm
    .idea /

    # Variables y secretos
    .env
    .env. *

    # Base de datos local
    db.sqlite3

    # Archivos estáticos recopilados
    staticfiles /

