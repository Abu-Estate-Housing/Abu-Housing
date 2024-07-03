from django.contrib import admin

from .models import Landlord, Staff, Tenant, User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("frist_name", "last_name", 'username', 'email')
    list_filter = ('role', 'is_active', )
    list_display = ("first_name", 'last_name', 'email', 'username', 'role', )


@admin.register(Landlord)
class LandlordAdmin(admin.ModelAdmin):
    search_fields = ("frist_name", "last_name", 'username', 'email')
    list_filter = ('role', 'is_active', )
    list_display = ("first_name", 'last_name', 'email', 'username', 'role', )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role=User.LANDLORD)

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    search_fields = ("frist_name", "last_name", 'username', 'email')
    list_filter = ('role', 'is_active', )
    list_display = ("first_name", 'last_name', 'email', 'username', 'role', )


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role=User.TENANT)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    search_fields = ("frist_name", "last_name", 'username', 'email')
    list_filter = ('role', 'is_active', )
    list_display = ("first_name", 'last_name', 'email', 'username', 'role', )


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_staff=True)
