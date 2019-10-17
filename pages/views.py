from django.shortcuts import render
from django.http import HttpResponse

from shelters.models import Shelter
from pets.models import Pet

# Create your views here.

def home(request):
    pets = Pet.objects.order_by('-list_date')[:3]

    context = {
        'pets': pets
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
