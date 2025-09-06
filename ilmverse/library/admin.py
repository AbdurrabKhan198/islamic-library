from django.contrib import admin

# Register your models here.
# library/admin.py

from django.contrib import admin
from .models import Book, Scholar, Category

admin.site.register(Book)
admin.site.register(Scholar)
admin.site.register(Category)
