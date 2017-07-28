from django import forms
from blog.models import Question
from django.forms import TextInput


class QuestionForm(forms.ModelForm):

	class Meta:
		model = Question
		fields = (
			'text',
			'is_anonymous',
			)
