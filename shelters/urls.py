from django.urls import path

from . import views

urlpatterns = [
    path('', views.shelters, name='shelters'),
    path('<int:shelter_id>', views.shelter, name='shelter'),
    path('search', views.search, name='ssearch'),
]
