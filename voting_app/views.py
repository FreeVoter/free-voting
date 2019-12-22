from django.shortcuts import render
from voting_app.topic import Topic
from voting_app import models
from voting_app import forms

topics = []
for i in range(0, len(models.Topic.objects.all())):
    topics.append(Topic())
    topics[i].load_from_model(models.Topic.objects.get(id=i))


def index_page(request):
    context = {'topics': topics}
    return render(request, 'index.html', context)


def topic_page(request):
    if request.method == "GET":
        current_topic = {'topic': topics[int(request.GET['id'])]}
        return render(request, 'topic.html', current_topic)
    elif "new_topic" in request.POST and request.POST["new_topic"] == '1':
        current_topic = {'topic': topics[int(request.GET['id'])], 'new_topic': True}
        return render(request, 'topic.html', current_topic)
    else:
        topics[int(request.GET['id'])].vote(int(request.POST['option_id']))
        current_topic = {'topic': topics[int(request.GET['id'])], 'option': int(request.POST['option_id']), 'voted': True}
        return render(request, 'topic.html', current_topic)


def user_page(request):
    return render(request, 'placeholder.html')


def new_topic_page(request):
    context = {'form': forms.AddTopicForm()}
    return render(request, 'new_topic.html', context)


def add_option_to_topic_page(request):
    form = forms.AddOptionToTopicForm()