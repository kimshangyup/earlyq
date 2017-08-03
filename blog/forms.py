from django import forms
from blog.models import Question, Channel
from django.forms import TextInput


class QuestionForm(forms.ModelForm):

	class Meta:
		model = Question
		fields = (
			'text',
			'is_anonymous',
			)


class ChannelForm(forms.ModelForm):

	class Meta:
		model = Channel
		fields = (
			'title',
			'description',
			'color',
			)
