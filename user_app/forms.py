from django import forms  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user_app.models import User 

class RegisterForm(UserCreationForm):
    """Register form"""  

    username = forms.CharField(max_length=255)
    class Meta:  
        model = User
        fields = ('email','username', 'password1', 'password2')  

        help_texts = {
            'username': '',
            'date_of_birth': '',
            'phone_number': '',
            'email': '',
            'password1': '',
            'password2': '',
        }

class LoginForm(AuthenticationForm):
     remember_me = forms.BooleanField(required=False)
