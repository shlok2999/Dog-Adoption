from django.contrib import admin

from .models import Pet

class PetAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'is_published', 'breed', 'list_date', 'shelter')
  list_display_links = ('id', 'name')
  list_filter = ('shelter', 'state')
  list_editable = ('is_published',)
  search_fields = ('name', 'state', 'breed')
  list_per_page = 25

admin.site.register(Pet, PetAdmin)
