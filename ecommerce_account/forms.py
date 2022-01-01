from django import forms
from ecommerce_user.models import User


class LoginUserForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': "input100"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "input100"}))


class RegisterUserForm(forms.Form):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': "input100"}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': "input100"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': "input100"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "input100"}))
    password2 = forms.CharField(label='confirm Password', widget=forms.PasswordInput(attrs={'class': "input100"}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('Email imported is repeated')

        return email
