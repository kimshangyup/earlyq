from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Question, Channel
from .forms import QuestionForm, ChannelForm


def channel_list(request):
    channels = Channel.objects.all()
    return render(request, 'blog/channel_list.html', locals())


@login_required
def channel_create(request):
    channel_form = ChannelForm(request.POST or None)
    if request.method == "POST":
        if channel_form.is_valid():
            form = channel_form.save(commit=False)
            form.creator = request.user
            form.save()
            return redirect('/blog/')
        else:
            return HttpResponse('error')
    else:
        pass    
    return render(request, 'blog/channel_create.html', locals())


@login_required
def channel_delete(request, pk):
    channel = Channel.objects.get(id=pk)
    if channel.creator == request.user:
        channel.delete()
        return redirect('/blog/')
    else:
        return HttpResponse('이 채널을 삭제할 권한이 없습니다')


def question_list(request, channel_pk):
    questions = Question.objects.filter(channel=channel_pk)
    channel = Channel.objects.get(id=channel_pk)
    return render(request, 'blog/question_list.html', locals())


def search(request):
    q = request.GET.get('q')
    questions = Question.objects.filter(text__icontains=q)
    return render(request, 'blog/question_list.html', locals())


@csrf_exempt
@login_required
def write(request):
    if not request.is_ajax():
        raise Http404('error')
    text = request.POST.get('new_question')
    is_anonymous = request.POST.get('is_anonymous')
    channel_id = request.POST.get('channel_id')
    channel = Channel.objects.get(id=channel_id)
    author = request.user
    if is_anonymous == '1':
        name = 'anonymous'
    else:
        name = author.username
    q = Question.objects.create(text=text, author=author, channel=channel, is_anonymous=is_anonymous)
    response_data = {
        'text': text,
        'author': name,
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
