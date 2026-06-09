from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superuser with specified credentials'

    def handle(self, *args, **options):
        username = 'tangyu'
        password = '221210'
        email = 'ty316319@163.com'
        first_name = '是唐哥哥啊'

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'User "{username}" already exists'))
            return

        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            first_name=first_name
        )
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully'))