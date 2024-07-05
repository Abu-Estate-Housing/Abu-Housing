from django.contrib import admin
from django.utils.html import format_html

from agreement.forms import AgreementAdminForm
from agreement.models import Agreement, Payment

# Register your models here.
@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    form = AgreementAdminForm

    list_display = ('property_name', 'price_in_naira', 'amount_paid', 'balance',  'status', 'start_date', 'end_date',)

    def balance(self, obj):
        balance = obj.price - obj.amount_paid
        formatted_price = "₦{:.2f}".format(balance)
        return format_html(formatted_price)

    def price_in_naira(self, obj):
        formatted_price = "₦{:.2f}".format(obj.price)
        return format_html(formatted_price)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('agreement', 'amount_paid', 'payment_date',)

    # def balance(self, obj):
    #     amount_paid = obj.agreement.amount_paid
    #     balance = obj.agreement.price - obj.amount_paid - amount_paid
    #     return balance

