from django.contrib import admin
from . models import Owner,Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'name', 'age', 'description')
    list_filter = ('name', 'kind', 'name', 'age')
    search_fields = ('name', 'kind', 'name', 'age', 'description')

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'mail', 'phone', 'get_animals')
    search_fields = ('name_surname', 'mail', 'phone')
    
    
