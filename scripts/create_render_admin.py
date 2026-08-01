#!/usr/bin/env python
import os
import django
from django.contrib.auth import get_user_model

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()
    User = get_user_model()

    username = os.environ.get('RENDER_ADMIN_USERNAME', 'admin')
    email = os.environ.get('RENDER_ADMIN_EMAIL', 'admin@example.com')
    password = os.environ.get('RENDER_ADMIN_PASSWORD', 'admin1234')

    if User.objects.filter(username=username).exists():
        print(f'Superusuario {username} ya existe. No se crea ninguno.')
        return

    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superusuario creado: {username}')

if __name__ == '__main__':
    main()
