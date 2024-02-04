from django.shortcuts import render
from pages.models import Socials


def home(request):
    return render(request, "pages/home.html", {})


def contact_me(request):
    socials = Socials.objects.all()
    context = {
        "socials" : socials
    }
    return render(request, "pages/contact_me.html", context)
