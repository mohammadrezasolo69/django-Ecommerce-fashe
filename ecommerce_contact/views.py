from django.contrib import messages
from django.shortcuts import render, redirect
from .models import ContactUs
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            full_name = cd['full_name']
            phone = cd['phone']
            email = cd['email']
            message = cd['message']
            new = ContactUs(full_name=full_name, email=email, phone=phone, message=message)
            new.save()
            messages.success(request, 'Your message was successfully sent .', 'success')
            return redirect('product:home')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', context={'form': form})
