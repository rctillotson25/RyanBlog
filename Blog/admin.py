from django.contrib import admin
from Blog.models import Post, PostCategory
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'date')
	list_filter = ['date']
	search_fields = ['title','body', 'body2']
	
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
