from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.conf import settings
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Create superuser from enviroment variables'
    
    def handle(self, *args, **Kwargs):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        
        if  not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS('Superuser created'))
        
        else:
            self.stdout.write(self.style.ERROR('Superuser already exists'))