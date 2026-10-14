from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created')
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'category', 'published')
    list_filter = ('category', 'author__username', 'published')
    search_fields = ('title', 'content', 'author__username', 'category__name')
    date_hierarchy = 'published'
    ordering = ('-published',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
