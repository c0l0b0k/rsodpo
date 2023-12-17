from django.db.models import Max, Q
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from teacher.forms import *

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from django.test import Client

import markdown

@csrf_exempt
def pivot_table_teacher(request):
    topics = Topic.objects.filter(subsection=None).order_by('topic_id')
    take_cookie = request.GET.get('take_cookie', None)
    if request.method == 'GET' and take_cookie==None:
        # Получаем преподавателя для текущего пользователя
        teacher = Teacher.objects.get(user=request.user)

        # Получаем все группы, связанные с этим преподавателем
        teacher_groups = teacher.groups.all()

        # Передаем только эти группы в форму
        form = PivotTableForm(groups=teacher_groups)

        context = {
            'user': request.user,
            'form': form,
            'topics':topics,
            'alphabet': 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ'
        }

        return render(request, 'pivottable.html', context)
    else:
        print("dfghgfdsdfghjhgfd")
        form = PivotTableForm(request.POST)
        data=form.data
        if (take_cookie):
            collapsed_nodes = request.session.get('collapsed_nodes')
        else:
            collapsed_nodes=form.data["collapsed_nodes"]
        request.session['collapsed_nodes'] = collapsed_nodes
        if collapsed_nodes:
            # Преобразование строки в список целых чисел
            collapsed_nodes = list(map(int, collapsed_nodes.split(',')))
        else:
            # Если строка пуста, создаем пустой список
            collapsed_nodes = []

        print(data)
        context = {
            'user': request.user,
            'form': form,
            'topics': topics,
            'alphabet': 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ',
            'collapsed_nodes': collapsed_nodes
        }
        if (take_cookie):
            group = request.session.get('study_group')
        else:
            group=data["study_group"]
        if group=="":
            teacher = Teacher.objects.get(user=request.user)
            teacher_groups = teacher.groups.all()
            group_ids =[group.group_id for group in teacher_groups]
        else:
            group_ids=[StudyGroup.objects.get(group_id=int(group)).group_id]
        if (take_cookie):
            selected_letter_name = request.session.get('selected_letter_name')
            selected_letter_surname = request.session.get('selected_letter_surname')
        else:
            selected_letter_name=data["selected_letter_name"]
            selected_letter_surname=data["selected_letter_surname"]
        students_filter = Q(study_group__group_id__in=group_ids)

        if selected_letter_name and selected_letter_name !="Все":
            students_filter &= Q(user__first_name__startswith=selected_letter_name)

        if selected_letter_surname and selected_letter_surname!="Все":
            students_filter &= Q(user__middle_name__startswith=selected_letter_surname)

        students = Student.objects.filter(students_filter)

        if (take_cookie):
            topic = request.session.get('selected_topic')
        else:
            topic=data["selected_topic"]

        if topic=="" or not (students.exists()):
            return render(request, 'pivottable.html', context)
        tasks=Task.objects.filter(topic_id=int(topic))
        latest_dates = Solution.objects.filter(task__in=tasks, student__in=students) \
            .values('task', 'student') \
            .annotate(max_date=Max('data_send'))

        # Получить соответствующие объекты Solution
        solutions = Solution.objects.filter(task__in=tasks, student__in=students,
                                            data_send__in=latest_dates.values('max_date'))
        context.update({'solutions': solutions})

        request.session['selected_letter_name'] = selected_letter_name
        request.session['selected_letter_surname'] = selected_letter_surname
        request.session['study_group'] = group

        request.session['selected_topic'] = topic

        return render(request, 'pivottable.html', context)




@csrf_exempt
def lab_view(request, solution_id=None):
    if request.method == 'GET':
        solution = Solution.objects.get(solution_id=solution_id)
        task = solution.task
        rate = Rate.objects.get(solution_id=solution.solution_id)
        python_code=solution.program_code
        # Подсветка кода
        lexer = get_lexer_by_name("python", stripall=True)
        formatter = HtmlFormatter(style="friendly", linenos=True, full=True)

        # Подсветка кода
        student_code = highlight(python_code, lexer, formatter)
        context = {
            'user': request.user,
            'task': task,
            'solution':solution,
            'rate':rate,
            'student_code':student_code,
        }

        return render(request, 'labview.html',context)
    if request.method == 'POST':

        # Отправьте POST-запрос на представление pivot_table_teacher
        target_url = '/pivot_table_teacher/?take_cookie=true'

        # Перенаправляем пользователя на целевое представление с использованием данных запроса
        return redirect(target_url)