from django.contrib.auth.models import User
from server.models import APIKey
import secrets

user = User.objects.get(id=1)  # получаем пользователя по ID
key = secrets.token_hex(20)  # генерируем случайный ключ
api_key = APIKey.objects.create(user=user, key=key)