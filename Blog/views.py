from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from Blog.models import Post

# Create your views here.
def index(request):
	latest_posts_list = Post.objects.order_by('-date')[:5]
	context = {'latest_posts_list': latest_posts_list}
	return render(request, 'blog/index.html', context)
	
def detail(request, post_id):
	try:
		post = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404
	return render(request, 'blog/detail.html', {'post' : post})
	
def results(request, post_id):
	return HttpResponse("You're looking at the results of post %s." % post_id)
	
def check(request, post_id):
	return HttpResponse("You're checking the results of post %s." % post_id)
	
