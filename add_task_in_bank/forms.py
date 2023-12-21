from django import  forms
from task.models import *
class AddTaskForm(forms.Form):
    topic = forms.ModelChoiceField(
        required=True,
        queryset=Topic.objects.filter(subsection=None).order_by('topic_id'),
        label="Тема"
    )
    subsection=forms.ModelChoiceField(required=True, queryset=Topic.objects.none(), label="Порядковый номер задания")
    task = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'aria-label': 'With textarea', 'style': 'height: 230px; resize: none;'})
    )
