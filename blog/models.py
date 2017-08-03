from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Channel(models.Model):
	title = models.CharField(max_length=255, verbose_name="그룹 이름")
	description = models.CharField(max_length=255, verbose_name="그룹 소개")
	creator = models.ForeignKey(User)
	color = models.CharField(max_length=10, verbose_name="색")


class Question(models.Model):
	text = models.TextField()
	channel = models.ForeignKey(Channel, related_name="questions")
	view = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name="asked")
	like = models.ManyToManyField(User, related_name="liked", blank=True)
	is_anonymous = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text
