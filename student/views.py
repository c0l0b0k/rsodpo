from collections import defaultdict
from itertools import groupby

from django.db.models import Max
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

from student.forms import LabViewForm
from task.models import *



@csrf_exempt
def task_view(request):
    # task_list_param = request.GET.get('task_list')
    # if task_list_param:
    #     task_list = [int(task_id) for task_id in task_list_param.split(',')]
    # # Ваш код здесь
    # current_student = get_object_or_404(Student, user=request.user)
    # task = Task.objects.get(pk=number)
    # topic= Topic.objects.get(pk = task.topic_id)
    # selected_solutions = Solution.objects.filter(student=current_student)
    # #all_related_tasks = [solution.task for solution in selected_solutions]
    #
    # solution=[solution.task for solution in selected_solutions if solution.task_id==number][0]
    # print(task_list)  # Печать числового значения
    # data={
    #     'user':request.user,
    #     'topic':topic.topic_name,
    #     'task':task.formulation,
    #     'solution':solution,
    #     'task_list':task_list
    # }
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
        if (solution):
            task = solution.task
            if solution.program_code:
                python_code = solution.program_code
                # Подсветка кода
                lexer = get_lexer_by_name("python", stripall=True)
                formatter = HtmlFormatter(style="friendly", linenos=True, full=True)

                # Подсветка кода
                student_code = highlight(python_code, lexer, formatter)

        print("-------")
        print(solution)
        print("-------")
        context={
            'topics':topics,
            'form': form,
            'collapsed_nodes': collapsed_nodes,
            'solution':solution,
            'task': task,
            'student_code': student_code,
        }
    return render(request,'labview.html',context)