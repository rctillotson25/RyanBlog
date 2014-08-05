from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from Blog.models import Post

# Create your views here.
def index(request):
	latest_posts_list = Post.objects.order_by('-date')[:5]
	template = loader.get_template('blog/index.html')
	context = RequestContext(request, {
		'latest_posts_list': latest_posts_list,
		})
	return HttpResponse(template.render(context))
	
def detail(request, post_id):
	return HttpResponse("You're looking at the post %s." % post_id)
	
def results(request, post_id):
	return HttpResponse("You're looking at the results of post %s." % post_id)
	
def check(request, post_id):
	return HttpResponse("You're checking the results of post %s." % post_id)
	
