from django.db import models
# from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField('auth.User', related_name="profile")
	nickname = models.CharField(max_length=20)
	thumbnail = models.ImageField(null=True, blank=True)
	# email = models.EmailField(max_length=100)

	def __str__(self):
		if self.nickname and self.nickname is not '':
			return self.nickname
		else:
			return self.user.username
