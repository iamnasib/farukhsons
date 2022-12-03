from django.contrib import admin
from . models import WorkImages,UserProfile,Invoice
# Register your models here.

admin.site.register(WorkImages)
admin.site.register(UserProfile)
admin.site.register(Invoice)