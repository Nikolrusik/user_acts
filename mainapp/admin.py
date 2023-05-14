from django.contrib import admin
from mainapp import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname',
                    'gender', 'blood_type', 'is_jobless', 'is_married']


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'city', 'address',
                    'postal_code', 'registered']


@admin.register(models.Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'description', 'estimation',
                    'date']
