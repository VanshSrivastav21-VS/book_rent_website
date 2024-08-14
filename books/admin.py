from django.contrib import admin
from .models import Book, Rental, News

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'rental_price', 'category', 'rented')
    list_filter = ('rented', 'category')
    search_fields = ('title', 'author', 'description')
    list_editable = ('rented', 'category')
    ordering = ('title',)
    fields = ('title', 'author', 'description', 'price', 'rental_price', 'image', 'sample_image', 'pages', 'rented', 'rent_end_date', 'category', 'pdf')

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rental_start_date', 'rental_end_date', 'is_returned')
    list_filter = ('is_returned', 'rental_start_date')
    search_fields = ('book__title', 'user__username')
    ordering = ('-rental_start_date',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)
    search_fields = ('title',)
    ordering = ('-date',)
    fields = ('title', 'date', 'image')
