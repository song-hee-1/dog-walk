from django.contrib import admin

from .models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'breed', 'birth', 'name', 'owner_id')


admin.site.register(Pet, PetAdmin)
