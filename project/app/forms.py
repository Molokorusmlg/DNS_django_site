from .models import Orders
from django import forms

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['date', 'email', 'number', 'product']