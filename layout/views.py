from __future__ import unicode_literals
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
    # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            sender = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")
            name = form.cleaned_data.get("full_name")
            phone = form.cleaned_data.get("phone")
            subject = "Contact Message"
            mail_message = " Name:%s \n\n Message: %s \n\n Email id: %s \n\n Phone number: %s" % \
                (name, message, sender, phone)
            from_email = sender
            to_email = [settings.EMAIL_HOST_USER]
            send_mail(subject,
                      mail_message,
                      from_email,
                      to_email,
                      fail_silently=True)
            for key, value in form.cleaned_data.items():
                print(key, value)
            messages.success(request, 'Mail send successfully')
        return HttpResponseRedirect('/home/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})
