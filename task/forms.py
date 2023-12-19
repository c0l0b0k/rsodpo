from django import  forms
from .models import *
from ckeditor.widgets import CKEditorWidget

class AddPostForm(forms.Form):
    task = forms.CharField(widget=CKEditorWidget(),label="Задание")
    choose_task=forms.ModelChoiceField(queryset=Task.objects.none(),label="Сушестующее задание")
    subsection=forms.ModelChoiceField(required=True, queryset= Topic.objects.none()  ,label="Порядковый номер задания")


    program_code = forms.CharField(widget=forms.Textarea(), label="Решение студента")

    topic = forms.ModelChoiceField(required=True, queryset=   Topic.objects.filter(subsection=None).order_by('topic_id'),label="Тема")
    new_topic = forms.CharField( required=True,label="Тема")
    sub_topic = forms.ModelChoiceField(required=False,empty_label="", queryset=Topic.objects.all(), label="Раздел")
    system_role_text=forms.CharField(required=False,widget=forms.Textarea(), label="Технические инстр. нс")

    model=forms.ModelChoiceField(required=True, queryset=  NeuralNetwork.objects.all(),label="Нс")


    recommend_text_neural = forms.CharField(widget=forms.Textarea(), label="Рекомендация нс")
    ideal_text_neural = forms.CharField(widget=forms.Textarea(), label="Эталонное решение")

class FillFromStorageForm(forms.Form):
    reqest_storage=forms.IntegerField( label="rate")
    kr1 = forms.IntegerField(required=False,label="Крритерий 1")
    kr2 = forms.IntegerField(required=False,label="Крритерий 2")
    kr3 = forms.IntegerField(required=False,label="Крритерий 3")
    kr4 = forms.IntegerField(required=False,label="Крритерий 4")
    kr5 = forms.IntegerField(required=False,label="Крритерий 5")
    kr6 = forms.IntegerField(required=False,label="Крритерий 6")
    kr7 = forms.IntegerField(required=False,label="Крритерий 7")
    kr8 = forms.IntegerField(required=False,label="Крритерий 8")
    kr9 = forms.IntegerField(required=False,label="Крритерий 9")
    kr10 = forms.IntegerField(required=False,label="Крритерий 10")

    recommend_text_neural = forms.CharField(required=False,widget=forms.Textarea(), label="Рекомендация нс")
    ideal_text_neural = forms.CharField(required=False,widget=forms.Textarea(), label="Эталонное решение")

    def clean(self):
        cleaned_data = super().clean()

        for field_name in self.fields:
            if field_name != 'reqest_storage':
                field_value = cleaned_data.get(field_name)
                if field_value is None:
                    cleaned_data[field_name] = None
        self.cleaned_data = cleaned_data

        return cleaned_data


