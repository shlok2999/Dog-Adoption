from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pets.choices import state_choices, breed_choices

from .models import Shelter
from pets.models import Pet

def shelters(request):
  shelters = Shelter.objects.order_by('-reg_date')

  paginator = Paginator(shelters, 6)
  page = request.GET.get('page')
  paged_shelters = paginator.get_page(page)

  context = {
    'shelters': paged_shelters,
    'state_choices': state_choices,
    'breed_choices': breed_choices,
  }

  return render(request, 'shelters/shelters.html', context)


def search(request):
  queryset_list = Shelter.objects.order_by('-reg_date')

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # # Breed
  # if 'breed' in request.GET:
  #   breed = request.GET['breed']
  #   if breed:
  #     queryset_list = queryset_list.filter(breed__iexact=breed)

  paginator = Paginator(queryset_list, 6)
  page = request.GET.get('page')
  paged_shelters = paginator.get_page(page)

  context = {
    'shelters': paged_shelters,
    'values': request.GET,
    'state_choices': state_choices,
    'breed_choices': breed_choices,
  }

  return render(request, 'shelters/search.html', context)

def shelter(request, shelter_id):
  shelter = get_object_or_404(Shelter, pk=shelter_id)
  pets = Pet.objects.filter(shelter_id__exact = shelter_id)

  paginator = Paginator(pets, 6)
  page = request.GET.get('page')
  paged_pets = paginator.get_page(page)

  context = {
    'shelter': shelter,
    'pets': paged_pets
  }

  return render(request, 'shelters/shelter.html', context)
