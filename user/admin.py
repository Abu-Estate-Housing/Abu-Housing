from django.contrib import admin

from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("frist_name", "last_name", 'username', 'email')
    list_filter = ('role', 'is_active', )
    list_display = ("first_name", 'last_name', 'email', 'username', 'role', )



