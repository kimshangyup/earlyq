from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# class LoginForm(AuthenticationForm):
#     email = forms.EmailField(label='이메일')

#     def clean_answer(self):
#         answer = self.cleaned_data['answer']
#         if answer != '6':
#             raise forms.ValidationError('땡~!!!')
#         return answer


class SignupForm(UserCreationForm):
    nickname = forms.CharField()
    # email = forms.EmailField()

    def save(self):
        user = super().save()

        nickname = self.cleaned_data['nickname']
        # email = self.cleaned_data['email']

        Profile.objects.create(user=user, nickname=nickname)

        return user