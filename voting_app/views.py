from django.shortcuts import render
from voting_app.topic import Topic

context = {'topics': [Topic(0, 'Как дела?', ['Отлично', 'Хорошо', 'Нормально', 'Плохо']),
                      Topic(1, 'За кого проголосуете?', ['За Путина', 'За Медведева']),
                      Topic(2, 'Что это за хрень?', ['роваотвпа', 'плвылитлчсвмвлаыо'])]}
# variables

# Create your views here.
def index_page(request):
    return render(request, 'index.html', context)


def topic_page(request):
    current_topic = {'topic': context['topics'][int(request.GET['id'])]}
    return render(request, 'topic.html', current_topic)


def vote_page(request):
    context['topics'][int(request.GET['id'])].vote(int(request.GET['option']))
    current_topic = {'topic': context['topics'][int(request.GET['id'])], 'option': int(request.GET['option'])}
    return render(request, 'vote.html', current_topic)


def user_page(request):
    current_user = {}
    return render(request, 'user.html', current_user)


def new_topic_page(request):
    return render(request, 'newtopic.html')