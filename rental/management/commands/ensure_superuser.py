from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from decouple import config


class Command(BaseCommand):
    help = "Create or update a Django superuser from environment variables."

    def handle(self, *args, **options):
        username = config("DJANGO_SUPERUSER_USERNAME", default="").strip()
        email = config("DJANGO_SUPERUSER_EMAIL", default="").strip()
        password = config("DJANGO_SUPERUSER_PASSWORD", default="").strip()

        if not username:
            self.stdout.write("No DJANGO_SUPERUSER_USERNAME set. Skipping admin user.")
            return

        if not password:
            password = get_random_string(32)
            self.stdout.write("No DJANGO_SUPERUSER_PASSWORD set. Generated a random password.")

        User = get_user_model()
        user, created = User.objects.get_or_create(username=username, defaults={"email": email})
        user.email = email or user.email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        action = "Created" if created else "Updated"
        self.stdout.write(self.style.SUCCESS(f"{action} superuser: {username}"))
