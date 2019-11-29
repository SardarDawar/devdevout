from django.contrib import admin
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget

class code_postAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'author', 'status']


class exampleAdmin(admin.ModelAdmin):
    list_filter = ('code_post',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Name',)}




admin.site.register(code_post, code_postAdmin)
admin.site.register(BlogAuthor)
admin.site.register(example, exampleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article)
admin.site.register(Sub_Category)





