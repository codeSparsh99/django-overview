from django.contrib import admin
from .models import UserCustom, Role, UserRole

# Register your models here.
admin.site.register(UserCustom)
admin.site.register(UserRole)
admin.site.register(Role)