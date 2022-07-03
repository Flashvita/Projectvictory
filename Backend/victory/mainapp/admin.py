from django.contrib import admin
from mainapp.models import Profile, Contact, Post, Team, Category


class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('user',)}
    list_display = ('user', 'created', 'phone', 'id')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'phone', )


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'id', 'parent', 'level', 'slug', 'road', 'children')


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'owner', 'id', 'created', 'is_active', 'is_private', 'category', 'road' )


class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Category, CategoryAdmin)
