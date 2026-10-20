from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

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
            "hours",
        )
        # Labels on signup form
        labels = {
            "username": "Create a username",
            "course": "Which course(s) would you like to tutor?",
            "name": "Enter your name",
            "hours": "What are your avaliable hours?"
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
    