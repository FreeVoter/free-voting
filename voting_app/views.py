from django.shortcuts import render
from voting_app.topic import Topic
from voting_app import models

topics = []
for i in range(0, len(models.Topic.objects.all())):
    topics.append(Topic())
    topics[i].load_from_model(models.Topic.objects.get(id=i))


def index_page(request):
    context = {'topics': topics}
    return render(request, 'index.html', context)


def topic_page(request):
    current_topic = {'topic': topics[int(request.GET['id'])]}
    return render(request, 'topic.html', current_topic)


def vote_page(request):
    topics[int(request.GET['id'])].vote(int(request.GET['option']))
    current_topic = {'topic': topics[int(request.GET['id'])], 'option': int(request.GET['option'])}
    return render(request, 'vote.html', current_topic)


def user_page(request):
    return render(request, 'placeholder.html')


def new_topic_page(request):
    return render(request, 'new_topic.html')
