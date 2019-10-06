"""Command-line utility for administrative tasks."""

import sys
import os
import environ
from django.core.management import execute_from_command_line


if __name__ == "__main__":
    ROOT_DIR = environ.Path(__file__) - 1
    env = environ.Env()
    env.read_env(str(ROOT_DIR.path('.env')))

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", env('DJANGO_SETTINGS_MODULE'))
    execute_from_command_line(sys.argv)
