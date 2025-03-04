from django.contrib import admin
from .models import *

# Register your models here.
class tododata(admin.ModelAdmin):
    list_display=['id', 'titel','completed']

admin.site.register(todo,tododata)