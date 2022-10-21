from django.contrib import admin
from .models import DataOrigin, DataSex, DataAge

# Register your models here.
admin.site.register(DataOrigin)
admin.site.register(DataSex)
admin.site.register(DataAge)