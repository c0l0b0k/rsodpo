from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from demo.forms import DemoForm
from demo.task import  sent_neuro_task
from task.models import *
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from django_rq import enqueue, job,  get_queue
import time, schedule

@job('default', timeout=600)
def run_sent_neuro_task(storage_id):
    print("tttt")
    sent_neuro_task(storage_id)

@csrf_exempt
def demo(request):
    form = DemoForm()
    contex = {
        'form': form
    }

    if request.method == 'POST':
        print(request.POST)
        data=request.POST
        task=data["task"]
        teacher = Teacher.objects.get(user=request.user)
        # t=Task.objects.create(formulation=task,key_words=preprocess_text(task), topic=Topic.objects.get(pk=data['subsection']))
        t = Task.objects.create(formulation=task,
                                topic=Topic.objects.get(pk=data['topic']))
        print("=======")
        s = Solution.objects.create(program_code=data['solution'],mark=-4, task=t)
        r = Rate.objects.create(solution=s)
        sr=StorageRequests.objects.create(is_done=False, rate=r,user=teacher)


        queue = get_queue('default')
        job = queue.enqueue(run_sent_neuro_task, sr.storage_id)
    return render(request, 'blank.html', contex)
@csrf_exempt
def reqvests_list(request):
    teacher = Teacher.objects.get(user=request.user)
    storage_requests = StorageRequests.objects.filter(user=teacher)
    contex = {
        'requests':storage_requests
    }
    return render(request, 'solutionstable.html', contex)

@csrf_exempt
def answer_view(request,storage_id):
    if request.method == 'GET':
        storage_request = StorageRequests.objects.get(pk=storage_id)
        program_code=storage_request.rate.solution.program_code
        lexer = get_lexer_by_name("python", stripall=True)
        formatter = HtmlFormatter(style="friendly", linenos=True, full=True)

        # Подсветка кода
        program_code = highlight(program_code, lexer, formatter)
        contex = {
            'request_id':storage_id,
            'task':storage_request.rate.solution.task.formulation,
            'program_code':program_code,
            'answer':storage_request.neural_answer
        }
        return render(request, 'labview_demo.html', contex)
    elif request.method == 'POST':
        storage_request = StorageRequests.objects.get(pk=storage_id)
        storage_request.delete()
        return redirect('reqvests_list')