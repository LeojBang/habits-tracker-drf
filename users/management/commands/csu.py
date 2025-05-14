from django.core.management.base import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CustomUser.objects.create(email="admin@gmail.com")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("w1s2x3")
        user.save()
