from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # Fields for users
        fields = (
            "username",
            "email",
            "age",
            "name",
            "course",
            "day",
        )
        # Labels on signup form
        labels = {
            "username": "Create a username",
            "course": "Which course(s) would you like to tutor?",
            "name": "Enter your name",
            "day": "What days are you avaliable?"
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
            "course",
        )
        
class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("day", "hours")
        labels = {
            "day": "Days available",
            "hours": "Available tutoring hours",
        }
    