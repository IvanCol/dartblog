from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Tag, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'created_at', 'updated_at', 'views', 'category', 'get_photo')
    list_display_links = ('title',)
    list_filter = ('category',)
    search_fields = ('title', 'tags', 'category', 'author')
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    save_on_top = True
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'author', 'content', 'get_photo', 'views', 'category', 'tags')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return '-'

    get_photo.short_description = 'Фотография'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
