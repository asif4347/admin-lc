from django.contrib import admin

# Register your models here.
from .models import Address, Configuration
admin.site.register(Address)
admin.site.register(Configuration)
