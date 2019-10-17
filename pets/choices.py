from .models import Pet

pets = Pet.objects.order_by('-list_date')

u_state_choices = dict()
state_choices = dict()
u_breed_choices = dict()
breed_choices = dict()

for pet in pets:
    if pet.state not in u_state_choices:
        type(pet.state)
        u_state_choices[str(pet.state)[:3].upper()] = str(pet.state)

    if pet.breed not in u_breed_choices:
        u_breed_choices[str(pet.breed)[:3].upper()] = str(pet.breed)
  
for key in sorted(u_state_choices.keys()):
    state_choices[key] = u_state_choices[key]
    
for key in sorted(u_breed_choices.keys()):
    breed_choices[key] = u_breed_choices[key]

print(state_choices)
print(breed_choices)



# state_choices = {

#     'D': 'Delhi',
#     'H': 'Haryana',
# }

# breed_choices = {

#     'B': 'Beagle',
#     'GS': 'German Shepherd',
#     'L': 'Labrador'
# }