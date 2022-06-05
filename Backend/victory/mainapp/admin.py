from django.contrib import admin
from mainapp.models import Profile, Contact, Post


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'phone', 'id')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'phone', )


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'id', 'created', 'is_active', 'is_private', )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Post, PostAdmin)
