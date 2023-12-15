from django.contrib import admin
from .models import  *
from django import  forms

@admin.register(AuthGroup)
class AuthGroupsAdmin(admin.ModelAdmin):
    list_display =('id','name')
    list_editable=('name',)
@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ('group_id','group_name')
    list_editable =('group_name',)
@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('spec_id','spec_name')
    list_editable =('spec_name',)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username')
    list_editable =('username',)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'education_level', 'get_username','study_group')
    list_editable = ('education_level','study_group')
    def get_username(self, obj):
        return obj.user.username
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',  'get_username')
    def get_username(self, obj):
        return obj.user.username
@admin.register(TeacherGroup)
class TeacherGroupAdmin(admin.ModelAdmin):
    list_display = ('teacher','group')



@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('rate_id','recommend_text','ideal_text','solution','neural')
    list_editable =('recommend_text','ideal_text','solution','neural')
@admin.register(NeuralNetwork)
class NeuralNetworkAdmin(admin.ModelAdmin):
    list_display = ('neural_id','neural_name')
    list_editable = ('neural_name',)
@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('solution_id','program_code','recommend_text','data_send','student','task')
    list_editable = ('program_code','data_send','task')
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_id','topic_name','subsection')
    list_editable = ('topic_name','subsection')
    list_display_links = ('topic_id',)

class TaskModelForm( forms.ModelForm ):
    formulation = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Task
        fields='__all__'
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    form = TaskModelForm
    list_display = ('task_id', 'formulation','topic', 'get_subsection_name')
    list_editable =( 'formulation','topic')
    @admin.display(description ='Subsection')
    def get_subsection_name(self, obj):
        return obj.topic.subsection.topic_name if obj.topic.subsection else None


