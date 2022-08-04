from django.contrib import admin

from .models import Walk


class WalkAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'distance', 'pet_id')


admin.site.register(Walk, WalkAdmin)
