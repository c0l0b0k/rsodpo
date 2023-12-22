from django import  forms
from task.models import  *
class PivotTableForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'Выберите...'),
        (1, 'Оценено'),
        (2, 'Возвращено'),
        (3, 'Ожидает проверки'),
        (4, 'Ожидает проверки ответ нс не пришёл'),

    ]


    def __init__(self, *args, **kwargs):
        groups = kwargs.pop('groups', None)
        super(PivotTableForm, self).__init__(*args, **kwargs)

        if groups:
            # Фильтруем группы, связанные с преподавателем
            self.fields['study_group'].queryset = groups

    study_group = forms.ModelChoiceField(empty_label="Все", queryset=StudyGroup.objects.all())
    status_solution = forms.ChoiceField(choices=STATUS_CHOICES)
    selected_letter_name=forms.CharField()
    selected_letter_surname=forms.CharField()
    collapsed_nodes = forms.CharField(required=False, widget=forms.HiddenInput())
    selected_topic=forms.CharField()


