from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.forms import PostForm, EmailForm
from blog.models import Post
from django.views.decorators.csrf import csrf_protect


def yoonzi(request):
    return render(request, 'yoonzi.html', locals())


def yoonzi1(request):
    return render(request, 'yoonzi1.html', locals())


def yoonzi2(request):
    return render(request, 'yoonzi2.html', locals())


def yoonzi3(request):
    return render(request, 'yoonzi3.html', locals())


def yoonzi4(request):
    return render(request, 'yoonzi4.html', locals())


@csrf_protect
def index(request):
    form = PostForm(request.POST or None)
    emailform = EmailForm()
    posts = Post.objects.all()[::-1]
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return render(request, 'index.html', locals())
        else:
            return HttpResponse('error')
    else:
        return render(request, 'index.html', locals())


@csrf_protect
def test(request):
    form = PostForm(request.POST or None)
    emailform = EmailForm()
    posts = Post.objects.all()[::-1]
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return render(request, 'test.html', locals())
        else:
            return HttpResponse('error')
    else:
        return render(request, 'test.html', locals())


@csrf_protect
def email(request):
    form = EmailForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog')
        else:
            return HttpResponse('error')
    else:
        return HttpResponse('error')