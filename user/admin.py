from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import path
from unfold.admin import ModelAdmin
from .models import Landlord, Staff, Tenant, User
from unfold.views import UnfoldModelAdminViewMixin
from django.views.generic import TemplateView

# Register your models here.

@admin.register(User)
class UserAdmin(ModelAdmin):

    search_fields = ("first_name", "last_name", "username", "email",)

    list_filter = ("role", "is_active",)
    list_display = ("first_name", "last_name", "email", "username", "role", "is_active")
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'username')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', )}),
        ('Important dates', {'fields': ('date_joined',)}),
        ('Roles', {'fields': ('role',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password', 'role'),
        }),
    )
    ordering = ('email',)


@admin.register(Landlord)
class LandlordAdmin(UserAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role=User.LANDLORD)

@admin.register(Tenant)
class TenantAdmin(UserAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role=User.TENANT)

@admin.register(Staff)
class StaffAdmin(ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_staff=True)



admin.site.unregister(Group)
