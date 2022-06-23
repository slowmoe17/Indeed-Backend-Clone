from django.contrib import admin
from .models import User, EmployeeProfile, EmployerProfile

admin.site.register(User)
admin.site.register(EmployeeProfile)
admin.site.register(EmployerProfile)