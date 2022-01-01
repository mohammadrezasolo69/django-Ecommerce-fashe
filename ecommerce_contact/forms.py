from django import forms
from .models import ContactUs


class ContactForm(forms.Form):
    full_name = forms.CharField(label='Full name', widget=forms.TextInput(
        attrs={'class': 'sizefull s-text7 p-l-22 p-r-22', 'placeholder': "Full Name"}))

    phone = forms.CharField(label='Phone', widget=forms.TextInput(
        attrs={'class': 'sizefull s-text7 p-l-22 p-r-22', 'placeholder': "Phone number"}))

    email = forms.CharField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'sizefull s-text7 p-l-22 p-r-22', 'placeholder': "Email"}))

    message = forms.CharField(label='Message', widget=forms.Textarea(
        attrs={'class': 'dis-block s-text7 size20 bo4 p-l-22 p-r-22 p-t-13 m-b-20', 'placeholder': "Message"}))
