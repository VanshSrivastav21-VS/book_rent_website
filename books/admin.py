from django.contrib import admin
from .models import Book, Rental

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'rental_price', 'rented', 'rent_end_date', 'category')
    search_fields = ('title', 'author', 'category')
    list_filter = ('author', 'rented', 'category')
    ordering = ('title',)
    readonly_fields = ('sample_image',)

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rental_start_date', 'rental_end_date', 'is_returned')
    list_filter = ('is_returned', 'rental_start_date', 'rental_end_date')
    search_fields = ('book__title', 'user__username')
    ordering = ('-rental_start_date',)
