from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms import TextInput

# class LoginForm(AuthenticationForm):
#     email = forms.EmailField(label='이메일')

#     def clean_answer(self):
#         answer = self.cleaned_data['answer']
#         if answer != '6':
#             raise forms.ValidationError('땡~!!!')
#         return answer



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('nickname', 'thumbnail',)
        widgets = {
            'nickname': TextInput(),
            # 'thumbnail': Select(choices=location_option, attrs={'class': 'form-control'})
        }



class SignupForm(UserCreationForm):
    nickname = forms.CharField()
    # email = forms.EmailField()

    def save(self):
        user = super().save()

        nickname = self.cleaned_data['nickname']
        # email = self.cleaned_data['email']

        Profile.objects.create(user=user, nickname=nickname)

        return user