from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    question = models.CharField(max_length=250)
    #author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def get_options(self):
        return Option.objects.filter(topic=self)

    def get_option(self, id_in_topic):
        return Option.objects.get(topic=self, id_in_topic=id_in_topic)


class Option(models.Model):
    id_in_topic = models.IntegerField()
    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE)
    option_name = models.CharField(max_length=250)
    votes = models.IntegerField()