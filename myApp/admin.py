from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):

    l=['name','marks','address','rollno']

admin.site.register(Student,StudentAdmin)
