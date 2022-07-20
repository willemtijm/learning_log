from django import forms
from .models import Topic

# Form based on the Topic model

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}