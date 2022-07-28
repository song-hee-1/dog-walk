from django.contrib import admin

from .models import Pet, Walk


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'breed', 'birth', 'name', 'owner_id')


class WalkAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'distance', 'pet_id')


admin.site.register(Pet, PetAdmin)
admin.site.register(Walk, WalkAdmin)
