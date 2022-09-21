from django.contrib import admin
from .models import Book, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'isbn']
    search_fields = ['title']


admin.site.register(Publisher)
