from django.contrib import admin
from.models import *
# Register your models here.
class TagTabularInline(admin.TabularInline):
    model = Tag

class PostAdmin(admin.ModelAdmin):
    inlines = [TagTabularInline]
    list_display = ['Title', 'Category','Author', 'Status', 'Main_Post', 'Date', 'Section']
    list_editable = ['Status','Category']
    search_fields = ['Title', 'Author', 'Category']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(ContactSubmission)


