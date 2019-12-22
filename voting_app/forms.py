from django import forms


class AddTopicForm(forms.Form):
    question = forms.CharField()
    # author = forms.CharField()


class AddOptionToTopicForm(forms.Form):
    topic_id = forms.IntegerField()
    option = forms.CharField()


class VoteForOptionForm(forms.Form):
    topic_id = forms.IntegerField()
    option_id = forms.IntegerField()
