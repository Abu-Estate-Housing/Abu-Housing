from datetime import datetime
from django.db import models
from property.models import Property
from user.models import Tenant


class Agreement(models.Model):
    COMPLETED = "completed"
    NOT_COMPLETED = "not-completed"

    STATUS = (
        (COMPLETED, COMPLETED),
        (NOT_COMPLETED, NOT_COMPLETED)
    )
    property_name = models.ForeignKey(Property, on_delete=models.CASCADE, null=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=False)
    status = models.CharField(max_length=50, choices=STATUS, null=False)
    price = models.FloatField(null=False)
    amount_paid = models.FloatField(default=0.0, null=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    reminder_sent = models.BooleanField(default=False, null=False)

    def __str__(self):
        end_year = self.end_date.strftime("%Y")
        return f'{self.property_name} for {end_year}'


class Payment(models.Model):
    agreement = models.ForeignKey(Agreement, on_delete=models.SET_NULL, null=True)
    amount_paid = models.FloatField(null=False)
    reciept = models.FileField(null=True, blank=True)
    payment_date = models.DateField(auto_now=True)
    settled = models.BooleanField(default=False)
    admin_note = models.TextField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
