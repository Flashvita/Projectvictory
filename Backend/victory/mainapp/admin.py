from django.contrib import admin
from mainapp.models import Profile, Contact, Post, Team, Category, Project


class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('user',)}
    list_display = ('user', 'role', 'phone', 'avatar', 'id', 'created', 'updated')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'phone', )


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'id', 'parent', 'level', 'slug', 'road')


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'owner', 'id', 'created', 'is_active', 'is_private', 'category', 'road' )


class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'id' )

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'id' )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
