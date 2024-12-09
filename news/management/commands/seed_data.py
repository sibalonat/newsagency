from django.core.management.base import BaseCommand
from news.models import User, Article
import lorem
import random

class Command(BaseCommand):
    help = 'Seed the database with initial users and articles'

    def handle(self, *args, **kwargs):
        users = [
            {'username': 'editor1', 'email': 'editor1@example.com', 'is_editor': True, 'is_reader': False},
            {'username': 'editor2', 'email': 'editor2@example.com', 'is_editor': True, 'is_reader': False},
            {'username': 'reader1', 'email': 'reader1@example.com', 'is_editor': False, 'is_reader': True},
            {'username': 'reader2', 'email': 'reader2@example.com', 'is_editor': False, 'is_reader': True},
            {'username': 'super', 'email': 'super@user.com', 'is_superuser': True, 'is_staff': True},
        ]

        for user_data in users:
            user, created = User.objects.get_or_create(username=user_data['username'], defaults=user_data)
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(self.style.SUCCESS(f"User '{user.username}' created"))
            else:
                self.stdout.write(self.style.WARNING(f"User '{user.username}' already exists"))

        # Create articles and assign them to one of the editors
        editors = User.objects.filter(is_editor=True)
        for i in range(30):  
            editor = random.choice(editors)
            title = lorem.sentence()
            content = [lorem.paragraph() for _ in range(5)]
            article = Article.objects.create(
                title=title,
                content='\n\n'.join(content),
                author=editor,
                image_url='https://i.postimg.cc/Zq4Syv95/output.jpg'
            )
            self.stdout.write(self.style.SUCCESS(f"Article '{article.title}' created by '{editor.username}'"))