from django.shortcuts import render
from django.contrib import messages
from .forms import HomeContactForm
from events.models import Programmes


def home(request):
    """
    View for rendering the home page.
    This view retrieves a list of active programs
    and displays them on the home page.
    It also handles a form submission for contacting the home page.
    """

    programmes = Programmes.objects.filter(status=1).order_by('?')[:3]
    text = "Your message is sent! We would get back to you soon!"

    if request.method == 'POST':
        home_contact_form = HomeContactForm(request.POST)

        if home_contact_form.is_valid():
            home_contact_form.save()
            messages.add_message(request, messages.SUCCESS, text)

    else:
        home_contact_form = HomeContactForm()

    return render(request, 'home/index.html', {
        'home_contact_form': home_contact_form,
        'programmes': programmes,
    })
