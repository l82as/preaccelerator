from django.contrib import admin
from .models import Page, TopMenu
# Register your models here.
class admPage(admin.ModelAdmin):
    list_display = ('title', 'create', 'update', 'published')
    list_display_links = ('title',)
    search_fields = ('title', 'body')
    list_editable = ('published',)
    list_filter = ('published', 'create')
    prepopulated_fields = {"slug":("title",)}
admin.site.register(Page, admPage)
admin.site.register(TopMenu)