from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'password '
        self.fields['password2'].label = 'repeat password '
        help_text = """
         <ol>
          <li>Your password can’t be too similar to your other personal information.</li>
          <li>Your password must contain at least 8 characters.</li>
          <li>Your password can’t be a commonly used password.</li>
          <li>Your password can’t be entirely numeric.</li>
        </ol> 
        """
        self.fields['password1'].help_text = help_text
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text =''

class SignUpView(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def logout_view(request):
    logout(request)