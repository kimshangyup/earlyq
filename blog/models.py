from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="글 제목")
    text = models.TextField(verbose_name="글 내용")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Email(models.Model):
    email = models.CharField(max_length=255)
