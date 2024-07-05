#!/usr/bin/env python3

from django import forms
from .models import Agreement, Tenant

class AgreementAdminForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AgreementAdminForm, self).__init__(*args, **kwargs)
        # Filter the tenant field to only include users with the Tenant role
        self.fields['tenant'].queryset = Tenant.objects.filter(role=Tenant.TENANT)
