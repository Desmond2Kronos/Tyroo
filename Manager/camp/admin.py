from django.contrib import admin
from camp.models import User, CampData

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(CampData)
