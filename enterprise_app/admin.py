from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Material, Client, Shoes, Production


   
admin.site.register(Material)
admin.site.register(Client)
admin.site.register(Shoes)
admin.site.register(Production)