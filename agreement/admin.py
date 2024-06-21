from django.contrib import admin

from agreement.models import Agreement, Payment

# Register your models here.
@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = ('property_name', 'price', 'amount_paid', 'balance',  'status', 'start_date', 'end_date',)

    def balance(self, obj):
        balance = obj.price - obj.amount_paid
        return balance


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('agreement', 'amount_paid', 'payment_date',)

    # def balance(self, obj):
    #     amount_paid = obj.agreement.amount_paid
    #     balance = obj.agreement.price - obj.amount_paid - amount_paid
    #     return balance

