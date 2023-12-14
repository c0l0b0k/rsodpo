

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse, HttpRequest
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
import g4f
from .models import *
from django.core import serializers
from task.forms import *
from task.util import*
from task.task import*
from django_rq import enqueue
import time, schedule
from django_rq import job
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import re
import os
import requests

@job('default', timeout=600)
def run_repeating_task():
    schedule.every(30).seconds.do(long_running_task)
    while True:
        schedule.run_pending()
        time.sleep(1)


def add(request):

    form = AddPostForm()
    data={
        'form':form
    }
    return render(request,'add.html',data)

@csrf_exempt
def fill_storage(request):

    # Передайте объекты в контекст шаблона
    if request.method =='POST':
        form = FillFromStorageForm(request.POST)
        form.is_valid()
        print("llllllllllllllllllllllll")


        request_=StorageRequests.objects.get(pk=form.cleaned_data['reqest_storage'])
        rate=Rate.objects.get(pk=request_.rate_id)
        rate.kr1 =form.cleaned_data["kr1"]
        rate.kr2 = form.cleaned_data["kr2"]
        rate.kr3 = form.cleaned_data["kr3"]
        rate.kr4 = form.cleaned_data["kr4"]
        rate.kr5 = form.cleaned_data["kr5"]
        rate.kr6 = form.cleaned_data["kr6"]
        rate.kr7 = form.cleaned_data["kr7"]
        rate.kr8 = form.cleaned_data["kr8"]
        rate.kr9 = form.cleaned_data["kr9"]
        rate.kr10 = form.cleaned_data["kr10"]
        rate.recommend_text=form.cleaned_data["recommend_text_neural"]
        rate.ideal_text=form.cleaned_data["ideal_text_neural"]
        rate.save()
        record_to_delete = StorageRequests.objects.get(pk=form.cleaned_data["reqest_storage"])
        record_to_delete.delete()

    else:
        form = FillFromStorageForm()
    request_=StorageRequests.objects.filter(is_done=True).first()


    rate = Rate.objects.get(pk=request_.rate_id)
    solution = Solution.objects.get(pk=rate.solution_id)
    task =Task.objects.get(pk=solution.task_id)
    topic = Topic.objects.get(pk=task.topic_id)
    promt=topic.system_text
    model=NeuralNetwork.objects.get(pk=rate.neural_id)
    neural_answer = request_.neural_answer
    reqest_storage=request_.storage_id
    print("------")
    print(task)
    print("------")
    form = FillFromStorageForm()
    context = {
            'form':form,
            'task':task.formulation,
            'solution':solution.program_code,
            'topic':topic.topic_name,
            'model':model.neural_name,
            'neural_answer':neural_answer,
            'reqest_storage':reqest_storage,
            'promt':promt
        }



    return render(request, 'fill_storage.html', context)


@csrf_exempt
def sent_neuro(request):
    print("dzfd")
    if request.method == 'POST':
        data = request.POST
        print(data)
        print("+++++++++")
        print(data["model"])

        system_role = Topic.objects.get(pk=data["topic"]).system_text
        print(system_role)
        content=get_clean_text(data["task"]) +"\n"+data["solution"]
        try:
            # Ваш код, который может вызвать исключение
            model = getattr(g4f.models, data["model"])
        except  :
            model=data["model"]
        response = g4f.ChatCompletion.create(
            model= model,
            messages=[{"role": "system", "content":system_role}, {"role": "user",
                                                                           "content": content}],

        )
        print(content)
        print(response)

        return JsonResponse({'message': 'Success', 'answer': response})
    else:
        return JsonResponse({'message': 'Error'}, status=400)


@csrf_exempt
def new_topic(request):
    data = request.POST

    sub_topic =Topic.objects.get(pk =data['sub_topic']) if data['sub_topic']!=""  else None

    t=Topic.objects.create(topic_name=data["new_topic"],system_text =data["system_role"], subsection= sub_topic)

    return JsonResponse({'message': 'Success', 'value': t.topic_id,'topic_name':t.topic_name})

def get_subsection_for_topic(request, topic_id):
    topic = get_object_or_404(Topic, topic_id=topic_id)
    topics = Topic.objects.filter(subsection=topic).order_by('topic_id')
    topic_list = [{'id': topic.topic_id, 'name': str(topic)} for topic in topics]
    return JsonResponse({'topics': topic_list})




@csrf_exempt
def add_request(request):

    data = request.POST
    task = data['task']
    saved_image_paths = process_and_save_images(task)

    # Замена src на путь до изображения в тексте
    for saved_image_path in saved_image_paths:
        relative_image_path = default_storage.url(saved_image_path)+"\" />"
        pattern = re.compile(r'data:image.*?/>')
        # Замена в тексте
        task = re.sub(pattern, relative_image_path, task)




    # t=Task.objects.create(formulation=task,key_words=preprocess_text(task), topic=Topic.objects.get(pk=data['subsection']))
    t = Task.objects.create(formulation=task,
                            topic=Topic.objects.get(pk=data['subsection']))


    s=Solution.objects.create(program_code=data['solution'],task=t)

    r1 = Rate.objects.create(solution=s, neural=NeuralNetwork.objects.get(neural_name="gpt-3.5-turbo-16k"))
    r2=Rate.objects.create(solution=s,neural=NeuralNetwork.objects.get(neural_name="gpt_4"))
    r3=Rate.objects.create(solution=s,neural=NeuralNetwork.objects.get(neural_name="gpt_35_turbo"))
    StorageRequests.objects.create(is_done=False,rate=r1)
    StorageRequests.objects.create(is_done=False, rate=r2)
    StorageRequests.objects.create(is_done=False, rate=r3)
    print(r1,r2,r3)
    return HttpResponse("OK")

@csrf_exempt
def start_fon_task(request):

    run_repeating_task()
    return HttpResponse("OK")

class login_user(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    extra_context = {'title': "Авторизация"}
    def get_success_url(self):
        user_group = self.request.user.groups.first()
        if user_group==None:
            return  reverse_lazy('admin:index')
        #if group_name == 'студенты':
        elif user_group.name=='Students':
            return reverse_lazy('home_student')
        elif user_group.name=='Teachers':
            return reverse_lazy('pivot_table_teacher')




