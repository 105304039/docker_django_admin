#!/usr/bin/env python
import os
import sys
import django


from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    
    
