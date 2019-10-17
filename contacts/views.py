from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    pet_id = request.POST['pet_id']
    pet = request.POST['pet']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    shelter_email = request.POST['shelter_email']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(pet_id=pet_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/pets/'+pet_id)

    contact = Contact(pet=pet, pet_id=pet_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    #Send email
    send_mail(
      'Pet Enquiry',
      'There has been an enquiry for ' + pet + '. Your response has been sent to respective shelter.',
      'dogadopt2019@gmail.com',
      [email, 'shelter_email'],
      fail_silently=False
     )

    messages.success(request, 'Your request has been submitted, a shelter representative will get back to you soon')
    return redirect('/pets/'+pet_id)
