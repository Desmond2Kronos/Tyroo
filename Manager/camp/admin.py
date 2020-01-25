from django.contrib import admin
from camp.models import User

admin.site.unregister(User)
admin.site.register(User)
