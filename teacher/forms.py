from django import  forms
from task.models import  *
class PivotTableForm(forms.Form):
    def __init__(self, *args, **kwargs):
        groups = kwargs.pop('groups', None)
        super(PivotTableForm, self).__init__(*args, **kwargs)

        if groups:
            # Фильтруем группы, связанные с преподавателем
            self.fields['study_group'].queryset = groups

    study_group = forms.ModelChoiceField(empty_label="Все", queryset=StudyGroup.objects.all())
