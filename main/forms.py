from django import forms
from .models import Review, Appointment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment", "image"]
        widgets = {
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
            "comment": forms.Textarea(attrs={"rows": 4}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "date",
            "time",
            "service",
            "client_name",
            "client_email",
            "client_phone",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "service": forms.Select(attrs={"class": "form-control"}),
            "client_name": forms.TextInput(attrs={"class": "form-control"}),
            "client_email": forms.EmailInput(attrs={"class": "form-control"}),
            "client_phone": forms.TextInput(attrs={"class": "form-control"}),
        }
