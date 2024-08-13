from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='books/images/')
    sample_image = models.ImageField(upload_to='books/sample/images/', null=True, blank=True)  # New field for sample image
    pages = models.IntegerField(default=100)
    rented = models.BooleanField(default=False)
    rent_end_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    is_returned = models.BooleanField(default=False)
