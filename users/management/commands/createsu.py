from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "This command creates superuser"

    def handle(self, *args, **options):
        admin = User.objects.get_or_none(username="chanadmin")
        if not admin:
            User.objects.create_superuser("chanadmin", "aksaksdm@naver.com", "youandme")
            self.stdout.write(self.style.SUCCESS(f"SuperUser created!"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser Exists"))
