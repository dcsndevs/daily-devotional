from django.shortcuts import render
from django.contrib import messages
from .forms import HomeContactForm

def home(request):

    if request.method == 'POST':
        home_contact_form = HomeContactForm(request.POST)
        if home_contact_form.is_valid():
            
            home_contact_form.save()
            messages.add_message(request, messages.SUCCESS, 
                                 "Your message is sent successfully! We would get back to you soon!")
 
    else:
        home_contact_form = HomeContactForm()
    return render(request, 'home/index.html', {'home_contact_form': home_contact_form})
