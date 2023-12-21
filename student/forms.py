from django import  forms
from task.models import  *
class LabViewForm(forms.Form):
    collapsed_nodes = forms.CharField(required=False, widget=forms.HiddenInput())
    selected_topic=forms.CharField()
