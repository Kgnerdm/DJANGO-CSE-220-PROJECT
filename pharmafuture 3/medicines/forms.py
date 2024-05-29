from django import forms
from .models import Medicine, HomeProduct

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'description', 'photo', 'price', 'category']  # Include category field
        
class HomeProductForm(forms.ModelForm):
    class Meta:
        model = HomeProduct
        fields = ['name', 'description', 'photo', 'price']
