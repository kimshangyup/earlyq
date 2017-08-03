from django.conf import settings
from django.shortcuts import redirect, render
from .forms import SignupForm
from django.contrib.auth.decorators import login_required


@login_required
def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			created_user = form.save()
			return redirect(settings.LOGIN_REDIRECT_URL)
	else:
		form = SignupForm()
	return render(request, 'accounts/signup.html', {	
		'form': form,
	})


def profile(request):
	return render(request, 'accounts/profile.html')
