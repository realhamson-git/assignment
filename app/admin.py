from django.contrib import admin
from .models import extendUser
# Register your models here.
@admin.register(extendUser)
class extendedAdmin(admin.ModelAdmin):
    list_display = ['user','address','types']