from django.db import models
from datetime import datetime
from shelters.models import Shelter
# Create your models here.


class Pet(models.Model):

    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)    
    dob = models.DateField()
    sex = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    state = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name