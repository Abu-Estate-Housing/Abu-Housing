
from django import forms
from .models import Property
from user.models import Tenant, Landlord

class PropertyAdminForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PropertyAdminForm, self).__init__(*args, **kwargs)
        # Filter the tenant field to only include users with the Tenant role
        self.fields['tenant'].queryset = Tenant.objects.filter(role=Tenant.TENANT)
        self.fields['landlord'].queryset = Tenant.objects.filter(role=Landlord.LANDLORD)
