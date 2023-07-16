from django.contrib import admin
from .models import Tasks
from .models import CustomUser

# Register your models here.
admin.site.register(CustomUser)

admin.site.register(Tasks)