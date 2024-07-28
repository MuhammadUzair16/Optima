
from django.shortcuts import render
from .models import AboutUs
from .models import Fact


def about_us(request):
    about = AboutUs.objects.first()  # Fetch the first entry or adjust as needed
    facts = Fact.objects.all()  # Fetch all facts
    return render(request, 'About/about.html', {'about': about, 'facts': facts})