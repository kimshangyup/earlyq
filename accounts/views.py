from django.conf import settings
from django.shortcuts import redirect, render
from .forms import SignupForm, ProfileForm
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			created_user = form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect(settings.LOGIN_REDIRECT_URL)
	else:
		form = SignupForm()
	return render(request, 'accounts/signup.html', {	
		'form': form,
	})


@login_required
def profile(request):
	form = ProfileForm(request.POST or None, request.FILES or None, instance=Profile.objects.get(user=request.user))
	if request.method == "POST":
		if form.is_valid():
			form.save()
			message = "성공적으로 반영되었습니다"
		else:
			return HttpResponse('error')
	else:
		pass
	return render(request, 'accounts/profile.html', locals())