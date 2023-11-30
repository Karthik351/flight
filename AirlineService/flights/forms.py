# AirlineService/forms.py

from django import forms
from .models import Passenger  # Import your models

class AddPassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger  # Use the appropriate model
        fields = ['Passenger_ID', 'First_Name', 'Last_Name', 'Email', 'Phone_Number', 'Age', 'Passport_Number']
