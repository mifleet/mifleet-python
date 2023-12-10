from django.contrib import admin
from rest_framework.authtoken.models import Token
from authentication.models import User

admin.site.register(User)