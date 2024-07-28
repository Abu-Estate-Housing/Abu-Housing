from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin

from agreement.forms import AgreementAdminForm
from agreement.models import Agreement, Payment

# Register your models here.
@admin.register(Agreement)
class AgreementAdmin(ModelAdmin):
    form = AgreementAdminForm

    list_display = ('property_name', 'price_in_naira', 'amount_paid_in_naira', 'balance',  'status', 'start_date', 'end_date',)

    def balance(self, obj):
        balance = obj.price - obj.amount_paid
        formatted_price = "₦{:.2f}".format(balance)
        return format_html(formatted_price)

    def price_in_naira(self, obj):
        formatted_price = "₦{:.2f}".format(obj.price)
        return format_html(formatted_price)

    def amount_paid_in_naira(self, obj):
        formatted_price = "₦{:.2f}".format(obj.amount_paid)
        return format_html(formatted_price)


@admin.register(Payment)
class PaymentAdmin(ModelAdmin):
    list_display = ('agreement', 'amount_paid_naira', 'payment_date', 'settled',)

    readonly_fields = ('agreement', 'settled',)

    def amount_paid_naira(self, obj):
        formatted_price = "₦{:.2f}".format(obj.amount_paid)
        return format_html(formatted_price)
