import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from users.models import Profile

for user in User.objects.all():
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
        print(f"Профиль создан для пользователя {user.username}")
    else:
        print(f"Пользователь {user.username} уже имеет профиль")