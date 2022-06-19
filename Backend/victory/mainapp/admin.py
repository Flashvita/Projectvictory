from django.contrib import admin
from mainapp.models import Profile, Contact, Post, Team, Category, SubCategory


class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('user',)}
    list_display = ('user', 'created', 'phone', 'id')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'phone', )


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'id', )


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'id', )


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'owner', 'id', 'created', 'is_active', 'is_private', 'subcategory' )


class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
