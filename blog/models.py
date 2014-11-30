from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
	tag_name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.tag_name

class Article(models.Model):
	author = models.ForeignKey(User, related_name='author')
	title = models.CharField(max_length=100)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title