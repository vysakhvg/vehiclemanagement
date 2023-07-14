from django import forms
from .models import vehicle_details


class Vehicleform(forms.ModelForm):
    class Meta:
        model = vehicle_details
        fields = ['id', 'vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']

        widgets = {
            'vehicle_number': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
            'vehicle_model': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_description': forms.Textarea(attrs={'class': 'form-control'}),
        }