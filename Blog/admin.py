from django.contrib import admin
from Blog.models import Post, PostCategory
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'date')
	list_filter = ['date']
	search_fields = ['title','body', 'body2']
	formfield_overrides = {
		models.CharField: {'widget': Textarea(attrs={'rows':5, 'cols':40})},
		models.TextField: {'widget': Textarea(attrs={'rows':25, 'cols':40})},
	}	
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
