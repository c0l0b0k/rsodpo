from django import  forms
from task.models import *
class DemoForm(forms.Form):
    topic = forms.ModelChoiceField(
        required=True,
        queryset=Topic.objects.filter(subsection=None).order_by('topic_id'),
        label="Тема"
    )
    task = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'aria-label': 'With textarea', 'style': 'height: 230px; resize: none;'})
    )
    solution = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'aria-label': 'With textarea', 'style': 'height: 230px; resize: none;'})
    )