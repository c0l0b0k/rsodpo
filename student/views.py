from collections import defaultdict
from itertools import groupby
from django.utils import timezone
from django.db.models import Max
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from student.tasks import *
from student.forms import LabViewForm
from task.models import *



@csrf_exempt
def task_view(request):

    topics = Topic.objects.filter(subsection=None).order_by('topic_id')
    student = Student.objects.get(user=request.user)
    if request.method == 'GET':
        form=LabViewForm()
        print("ggggg")
        print(topics)
        context={
            'topics':topics,
            'form': form,
                 }
    if request.method == 'POST':
        form=LabViewForm(request.POST)
        data = form.data

        task=None
        rate=None
        student_code=None
        mark=None


        collapsed_nodes=form.data["collapsed_nodes"]
        if collapsed_nodes:
            # Преобразование строки в список целых чисел
            collapsed_nodes = list(map(int, collapsed_nodes.split(',')))
        else:
            # Если строка пуста, создаем пустой список
            collapsed_nodes = []


        topic = data["selected_topic"]
        tasks = Task.objects.filter(topic_id=int(topic))

        latest_dates = Solution.objects.filter(task__in=tasks, student=student) \
            .values('task', 'student') \
            .annotate(max_date=Max('data_send'))

        # Получить соответствующие объекты Solution
        solution = Solution.objects.filter(task__in=tasks, student=student,
                                            data_send__in=latest_dates.values('max_date')).first()

        status_solutuion=int(data["status_solution"])


        if (solution):
            task = solution.task
            print("kkkkkkkkkkk")

            print("wwwwwww")
            print(solution.mark)
            print(data["status_solution"])
            print("wwwwwww")
            if(solution.mark==-1  and status_solutuion==2):
                print("oooooooooo")
                solution.program_code=data["solution"]
                solution.mark=-2
                solution.data_send = timezone.now()
                solution.save()
                rate=Rate.objects.create(solution=solution,neural=task.best_model)
                sr=StorageRequests.objects.create(is_done=False, rate=rate)
                send_student_code.delay(sr.storage_id)

            elif(status_solutuion==3):
                solution = Solution.objects.create(student=student, task=task, data_send=timezone.now(), program_code=data["solution"],
                                    mark=-2)
                print("33333333333333")
                print(data["solution"])
                print("33333333333333")

            elif(solution.mark in [0,-2,-3] and status_solutuion==1):
                print("yyyyyyyyyyyyyyyyyyyyyyyyyyyy")
                solution=Solution(student=student,task=task, data_send =timezone.now(),program_code=data["solution"],mark=-4)


                # rate = Rate.objects.create(solution=solution, neural=task.best_model)
                # sr = StorageRequests.objects.create(is_done=False, rate=rate)
                # send_student_code.delay(sr.storage_id)
            if   solution.program_code:
                python_code = solution.program_code
                # Подсветка кода
                lexer = get_lexer_by_name("python", stripall=True)
                formatter = HtmlFormatter(style="friendly", linenos=True, full=True)

                # Подсветка кода
                student_code = highlight(python_code, lexer, formatter)



        context={
            'topics':topics,
            'form': form,
            'collapsed_nodes': collapsed_nodes,
            'solution':solution,
            'task': task,
            'student_code': student_code,
        }
    return render(request,'labview_stud.html',context)

def solution_list(request, task_id):
    student = Student.objects.get(user=request.user)
    task=Task.objects.get(pk=task_id)
    solutions = Solution.objects.filter(task=task, student=student).order_by("data_send")
    context={
        'solutions':solutions
    }
    return render(request,'solutionstable.html',context)