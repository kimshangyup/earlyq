from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
	text = models.TextField()
	view = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name="asked")
	like = models.ManyToManyField(User, related_name="liked", blank=True)
	is_anonymous = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text
