from ckeditor_uploader import forms
from django.contrib import admin
from .models import Page, TopMenu

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PageAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Page

class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm

admin.site.register(Page, PageAdmin)

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