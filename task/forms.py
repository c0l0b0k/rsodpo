from django import  forms
from .models import *

class AddPostForm(forms.Form):
    task = forms.CharField(widget=forms.Textarea(),label="Задание")
    choose_task=forms.ModelChoiceField(queryset=Task.objects.all(),label="Сушестующее задание")
    difficulty =forms.IntegerField( required=True,label="Сложность")

    program_code = forms.CharField(widget=forms.Textarea(), label="Решение студента")

    topic = forms.ModelChoiceField(required=True, queryset=  Topic.objects.all(),label="Тема")
    new_topic = forms.CharField( required=True,label="Тема")
    sub_topic = forms.ModelChoiceField(required=False,empty_label="", queryset=Topic.objects.all(), label="Раздел")
    system_role_text=forms.CharField(required=False,widget=forms.Textarea(), label="Технические инстр. нс")


    model=forms.ModelChoiceField(required=True, queryset=  NeuralNetwork.objects.all(),label="Нс")

    errors_neural = forms.CharField(widget=forms.Textarea(), label="Ошибки от нейроной сети")
    recommend_text_neural = forms.CharField(widget=forms.Textarea(), label="Рекомендация нс")
    ideal_text_neural = forms.CharField(widget=forms.Textarea(), label="Эталонное решение")

class FillFromStorageForm(forms.Form):
    reqest_storage=forms.IntegerField( label="rate")
    kr1 = forms.IntegerField(label="Крритерий 1")
    kr2 = forms.IntegerField(label="Крритерий 2")
    kr3 = forms.IntegerField(label="Крритерий 3")
    kr4 = forms.IntegerField(label="Крритерий 4")
    kr5 = forms.IntegerField(label="Крритерий 5")
    kr6 = forms.IntegerField(label="Крритерий 6")
    kr7 = forms.IntegerField(label="Крритерий 7")
    kr8 = forms.IntegerField(label="Крритерий 8")
    kr9 = forms.IntegerField(label="Крритерий 8")
    kr10 = forms.IntegerField(label="Крритерий 9")
    errors_neural = forms.CharField(widget=forms.Textarea(), label="Ошибки от нейроной сети")
    recommend_text_neural = forms.CharField(widget=forms.Textarea(), label="Рекомендация нс")
    ideal_text_neural = forms.CharField(widget=forms.Textarea(), label="Эталонное решение")


