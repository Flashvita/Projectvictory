from django.contrib import admin
from mainapp.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'phone', 'id')


admin.site.register(Profile, ProfileAdmin)
