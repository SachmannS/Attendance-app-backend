from django.contrib import admin
from .models import Profile, Organisation
# Register your models here.

admin.site.register(Organisation)
admin.site.register(Profile)