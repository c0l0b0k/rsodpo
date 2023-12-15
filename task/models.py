from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
class User(AbstractUser):
    middle_name = models.CharField(blank=True, null=True)
    corp_mail = models.CharField(blank=True, null=True)

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class StorageRequests(models.Model):
     storage_id=models.AutoField(primary_key=True)
     neural_answer=models.CharField(blank=True, null=True)
     is_done =models.BooleanField(blank=True, null=True)
     rate=models.ForeignKey('Rate', models.DO_NOTHING, blank=True, null=True)
     class Meta:
         managed = True
         db_table = 'storage_requests'



class NeuralNetwork(models.Model):
    neural_id = models.AutoField(primary_key=True)
    neural_name = models.CharField()


    def __str__(self):
        return self.neural_name

    class Meta:
        managed = True
        db_table = 'neural_network'






class Rate(models.Model):
    rate_id = models.AutoField(primary_key=True)
    kr1=models.IntegerField(blank=True, null=True)
    kr2=models.IntegerField(blank=True, null=True)
    kr3=models.IntegerField(blank=True, null=True)
    kr4=models.IntegerField(blank=True, null=True)
    kr5=models.IntegerField(blank=True, null=True)
    kr6=models.IntegerField(blank=True, null=True)
    kr7=models.IntegerField(blank=True, null=True)
    kr8=models.IntegerField(blank=True, null=True)
    kr9=models.IntegerField(blank=True, null=True)
    kr10=models.IntegerField(blank=True, null=True)
    recommend_text = models.CharField(blank=True, null=True)
    ideal_text = models.CharField(blank=True, null=True)
    solution = models.ForeignKey('Solution', models.DO_NOTHING,related_name='rates' , blank=True, null=True)
    neural = models.ForeignKey(NeuralNetwork, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rate'


class Solution(models.Model):
    solution_id = models.AutoField(primary_key=True)
    program_code = models.CharField(blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)
    recommend_text = models.CharField(blank=True, null=True)
    data_send= models.DateTimeField(blank=True, null=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)
    task = models.ForeignKey('Task', models.DO_NOTHING, blank=True, null=True, related_name='solutions')


    def __str__(self):
        if self.program_code!=None:
            return self.program_code
        else:
            return str(self.solution_id)


    class Meta:
        managed = True
        db_table = 'solution'



class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    formulation =  RichTextField()
    max_mark=models.CharField(blank=True, null=True)
    key_words= models.CharField(blank=True, null=True)
    topic = models.ForeignKey('Topic', models.DO_NOTHING, blank=True, null=False)

    def __str__(self):
        return self.formulation[:100]
    class Meta:
        managed = True
        db_table = 'task'

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    topic_name = models.CharField()
    system_text = models.CharField(blank=True, null=True)
    subsection = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, unique=False)
    def __str__(self):
        return self.topic_name

    def as_json(self):
        return dict(
            input_id=self.topic_id,
            topic_name=self.topic_name)
    class Meta:
        managed = True
        db_table = 'topic'



class Speciality(models.Model):
    spec_id = models.AutoField(primary_key=True)
    spec_name = models.CharField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'speciality'

class Student(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    education_level = models.CharField(blank=True, null=True)
    spec = models.ForeignKey(Speciality, models.DO_NOTHING, blank=True, null=True)
    study_group = models.ForeignKey('StudyGroup', models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
        return self.user.corp_mail

    def get_full_name(self):
        return f"{self.user.middle_name} {self.user.first_name} {self.user.last_name}"
    class Meta:
        managed = True
        db_table = 'student'

class StudyGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField()


    class Meta:
        managed = True
        db_table = 'study_group'
    def __str__(self):
        return self.group_name



class Teacher(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    post_name = models.CharField(blank=True, null=True)
    groups = models.ManyToManyField(StudyGroup, through='TeacherGroup')

    def __str__(self):
        return self.user.corp_mail
    class Meta:
        managed = True
        db_table = 'teacher'


class TeacherGroup(models.Model):
    teacher = models.ForeignKey(Teacher, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(StudyGroup, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'teacher_group'
