from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Question
from .forms import QuestionForm


def index(request):
    questions = Question.objects.all()
    return render(request, 'blog/index.html', locals())


def search(request):
    q = request.GET.get('q')
    questions = Question.objects.filter(text__icontains=q)
    return render(request, 'blog/index.html', locals())


@csrf_exempt
@login_required
def write(request):
    if not request.is_ajax():
        raise Http404('error')
    text = request.POST.get('new_question')
    author = request.user
    q = Question.objects.create(text=text, author=author)
    response_data = {
        'text': text,
        'author': author.username,
        'id': q.id
    }
    return JsonResponse(response_data)


@csrf_exempt
@login_required
def delete(request, pk):
    if not request.is_ajax():
        raise Http404('error')
    q = Question.objects.get(id=pk)
    q.delete()
    response_data = {}
    return JsonResponse(response_data)
