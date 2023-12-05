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

@job('default', timeout=600)
def run_repeating_task():
    schedule.every(30).seconds.do(long_running_task)
    while True:
        schedule.run_pending()
        time.sleep(1)


def add(request):
    # Вроде как этот код не нужен
    # if request.method =='POST':
    #
    #     form = AddPostForm(request.POST)
    #
    #     t1=Task.objects.create(formulation=form.data['task'],topic=Topic.objects.get(pk=form.data['topic']))
    #     s1=Solution.objects.create(program_code=form.data['program_code'],recommend_text=form.data['recommend_text'],errors_text = form.data['errors'],task=t1)
    #     r1=Rate.objects.create(errors_rate=form.data['errors_rate'],recommend_rate=form.data['recommend_rate'],ideal_rate=form.data['ideal_rate'],recommend_text=form.data['recommend_text_neural'], ideal_text=form.data['ideal_text_neural'],solution=s1,neural=NeuralNetwork.objects.get(pk =form.data['neural_network']))
    #
    #
    # else:
    #     form =  AddPostForm()
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
        print("llllllllllllllllllllllll")

        data=(form.data)
        print(data)
        request_=StorageRequests.objects.get(pk=data['reqest_storage'])
        rate=Rate.objects.get(pk=request_.rate_id)
        rate.kr1 =data["kr1"]
        rate.kr2 = data["kr2"]
        rate.kr3 = data["kr3"]
        rate.kr4 = data["kr4"]
        rate.kr5 = data["kr5"]
        rate.kr6 = data["kr6"]
        rate.kr7 = data["kr7"]
        rate.kr8 = data["kr8"]
        rate.kr9 = data["kr9"]
        rate.kr10 = data["kr10"]
        rate.errors_text=data["errors_neural"]
        rate.recommend_text=data["recommend_text_neural"]
        rate.ideal_text=data["ideal_text_neural"]
        rate.save()
        record_to_delete = StorageRequests.objects.get(pk=data["reqest_storage"])
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
        content=data["task"] +"\n"+data["solution"]
        response = g4f.ChatCompletion.create(
            model= getattr(g4f.models, data["model"]),
            messages=[{"role": "system", "content":system_role}, {"role": "user",
                                                                           "content": content}],
            provider=g4f.Provider.GptForLove
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

def get_tasks_for_topic(request, topic_id):
    topic = get_object_or_404(Topic, topic_id=topic_id)
    tasks = Task.objects.filter(topic=topic)
    task_list = [{'id': task.task_id, 'name': str(task)} for task in tasks]
    return JsonResponse({'tasks': task_list})

#Вроде можно удалить
# @csrf_exempt
# def new_neuro(request):
#     data = request.POST
#     print(data)
#     n = NeuralNetwork.objects.create(neural_name=data["new_neuro"])
#
#     return JsonResponse({'message': 'Success', 'value': n.neural_id, 'neuro_name': n.neural_name})


@csrf_exempt
def add_request(request):
    data = request.POST
    print("jjjjjjjjjjj")
    print(data)
    if data["task_id"]=="":
        t=Task.objects.create(formulation=data['task'], topic=Topic.objects.get(pk=data['topic']),difficulty=data['difficulty'])
    else:
        t=Task.objects.get(pk=data['task_id'])

    s=Solution.objects.create(program_code=data['solution'],task=t)

    r1 = Rate.objects.create(solution=s, neural=NeuralNetwork.objects.get(neural_name="claude_v1"))
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
            return reverse_lazy('home_teachers')
