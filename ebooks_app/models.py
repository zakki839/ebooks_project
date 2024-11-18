
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):  # Changed class name to Category (uppercase C)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ordering=['name']
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True, help_text='Book Title', error_messages={'unique': 'Book title must be unique'})
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Corrected reference to Category
    book_cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    description = models.TextField()
    published_date = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')])

    def __str__(self):
        return self.title
