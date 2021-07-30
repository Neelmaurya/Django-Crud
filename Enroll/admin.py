from django.contrib import admin
from .models import Registration, Student
# Register your models here.

@admin.register(Registration)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dob', 'email', 'mobile', 'pwd')

@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dob', 'email', 'mobile', 'password')