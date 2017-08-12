from django import forms
from blog.models import Question, Channel
from django.forms import TextInput, Select


class QuestionForm(forms.ModelForm):

	class Meta:
		model = Question
		fields = (
			'text',
			'is_anonymous',
			)


color_option = (
    ('blue', 'blue'),
    ('pink', 'pink'),
    ('purple', 'purple'),
    ('green', 'green'),
    ('yellow', 'yellow'),
)

class ChannelForm(forms.ModelForm):

	class Meta:
		model = Channel
		fields = (
			'title',
			'description',
			'color',
			)
		widgets = {
            'title': TextInput(attrs={'placeholder': "Group Name"}),
            'description': TextInput(attrs={'placeholder': "Group Description"}),
            'color': Select(choices=color_option)
        }

