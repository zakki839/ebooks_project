from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Category, Book

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'profile_picture', 'date_of_birth', 'location', 'website')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Display the name and description fields
    search_fields = ('name',)  # 'name' should be in a tuple
    list_filter = ('name',)  # Filter by name

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book)
