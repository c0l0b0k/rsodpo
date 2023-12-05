from collections import defaultdict
from itertools import groupby

from django.shortcuts import render, get_object_or_404

from task.models import *


def home_student(request):
    topic_list = Topic.objects.all().order_by("topic_id")

    current_student = get_object_or_404(Student, user=request.user)
    selected_solutions = Solution.objects.filter(student = current_student)
    all_related_tasks = [solution.task for solution in selected_solutions]
    print(all_related_tasks)
    sorted_related_tasks = sorted(all_related_tasks, key=lambda task: task.topic_id)
    print(sorted_related_tasks)
    grouped_tasks = defaultdict(list)

    for task in all_related_tasks:
        grouped_tasks[task.topic.topic_id].append(task)

    # Теперь сортируем каждый список в словаре по полю difficulty
    for key in grouped_tasks:
        grouped_tasks[key] = sorted(grouped_tasks[key], key=lambda task: task.difficulty)
    print(grouped_tasks)

    data = {
        'user': request.user,
        'topic_list':topic_list,
        'grouped_tasks':grouped_tasks
    }
    return render(request,'studenthomepage.html',context=data)


def task_view(request, number):
    task_list_param = request.GET.get('task_list')
    if task_list_param:
        task_list = [int(task_id) for task_id in task_list_param.split(',')]
    # Ваш код здесь
    current_student = get_object_or_404(Student, user=request.user)
    task = Task.objects.get(pk=number)
    topic= Topic.objects.get(pk = task.topic_id)
    selected_solutions = Solution.objects.filter(student=current_student)
    #all_related_tasks = [solution.task for solution in selected_solutions]

    solution=[solution.task for solution in selected_solutions if solution.task_id==number][0]
    print(task_list)  # Печать числового значения
    data={
        'user':request.user,
        'topic':topic.topic_name,
        'task':task.formulation,
        'solution':solution,
        'task_list':task_list
    }
    return render(request,'labviewpage.html',data)