from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from profiles.models import UserProfile
from django.contrib import messages

# Create your views here.


def index(request):
    """ Return the index page """

    return render(request, 'home/index.html')


def contact_us(request):
    """
    Contact form to post query to gmail account
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            sender_name = form.cleaned_data['contact_name']
            sender_email = form.cleaned_data['contact_email']
            sender_query = form.cleaned_data['query']
            sender_message = form.cleaned_data['message']
            recipient = settings.EMAIL_HOST_USER

            # Email template
            message = ("Name: {0}\nEmail: {1}\n\nMessage:\n{2}".format
                       (sender_name, sender_email, sender_message))
            send_mail(sender_query, message, sender_email,
                      [recipient])

            messages.success(request, "Message sent!")

    return redirect(reverse("home"))
