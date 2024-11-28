from django.core.management.base import BaseCommand
from news.models import User

class Command(BaseCommand):
    help = 'Seed the database with initial users'

    def handle(self, *args, **kwargs):
        users = [
            {'username': 'editor1', 'email': 'editor1@example.com', 'is_editor': True, 'is_reader': False},
            {'username': 'editor2', 'email': 'editor2@example.com', 'is_editor': True, 'is_reader': False},
            {'username': 'reader1', 'email': 'reader1@example.com', 'is_editor': False, 'is_reader': True},
            {'username': 'reader2', 'email': 'reader2@example.com', 'is_editor': False, 'is_reader': True},
        ]

        for user_data in users:
            user, created = User.objects.get_or_create(username=user_data['username'], defaults=user_data)
            if created:
                user.set_password('password123')  # Set a default password
                user.save()
                self.stdout.write(self.style.SUCCESS(f"User '{user.username}' created"))
            else:
                self.stdout.write(self.style.WARNING(f"User '{user.username}' already exists"))