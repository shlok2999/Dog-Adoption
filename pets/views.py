from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .choices import state_choices, breed_choices

from .models import Pet

def index(request):
  pets = Pet.objects.order_by('-list_date')

  paginator = Paginator(pets, 6)
  page = request.GET.get('page')
  paged_pets = paginator.get_page(page)

  context = {
    'pets': paged_pets,
    'breed_choices': breed_choices,
    'state_choices': state_choices,
  }

  return render(request, 'pets/pets.html', context)

  

def search(request):
  queryset_list = Pet.objects.order_by('-list_date')

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Breed
  if 'breed' in request.GET:
    breed = request.GET['breed']
    if breed:
      queryset_list = queryset_list.filter(breed__iexact=breed)

  paginator = Paginator(queryset_list, 6)
  page = request.GET.get('page')
  paged_pets = paginator.get_page(page)

  context = {
    'pets': paged_pets,
    'values': request.GET,
    'breed_choices': breed_choices,
    'state_choices': state_choices,
  }
  return render(request, 'pets/search.html', context)

# @login_required(login_url='login')
def pet(request, pet_id):
  pet = get_object_or_404(Pet, pk=pet_id)

  context = {
    'pet': pet,
  }

  print(pet.shelter.id)
  if not request.user.is_authenticated:
    messages.warning(request, 'You have to Login/Register make an enquiry for adoption of this pet')
    
    
  return render(request, 'pets/pet.html', context)