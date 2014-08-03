from django.db import models

# Create your models here.



class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.CharField(max_length=8000)
	body2 = models.CharField(max_length=8000)
	date = models.DateTimeField('date created')
	category = models.ForeignKey(PostCategory)
	
class PostCategory(models.Model):
	description(models.CharField(max_length=200)