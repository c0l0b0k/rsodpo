from django.db.models import Max, Q
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from teacher.forms import *

@csrf_exempt
def pivot_table_teacher(request):
    topics = Topic.objects.filter(subsection=None).order_by('topic_id')
    if request.method == 'GET':
        # Получаем преподавателя для текущего пользователя
        teacher = Teacher.objects.get(user=request.user)

        # Получаем все группы, связанные с этим преподавателем
        teacher_groups = teacher.groups.all()

        # Передаем только эти группы в форму
        form = PivotTableForm(groups=teacher_groups)

        data = {
            'user': request.user,
            'form': form,
            'topics':topics,
            'alphabet': 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ'
        }

        return render(request, 'pivottable.html', data)
    elif request.method == 'POST':
        form = PivotTableForm(request.POST)
        data=form.data



        collapsed_nodes=form.data["collapsed_nodes"]
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

        group=data["study_group"]
        if group=="":
            teacher = Teacher.objects.get(user=request.user)
            teacher_groups = teacher.groups.all()
            group_ids =[group.group_id for group in teacher_groups]
        else:
            group_ids=[StudyGroup.objects.get(group_id=int(group)).group_id]
        selected_letter_name=data["selected_letter_name"]
        selected_letter_surname=data["selected_letter_surname"]
        students_filter = Q(study_group__group_id__in=group_ids)

        if selected_letter_name and selected_letter_name !="Все":
            students_filter &= Q(user__first_name__startswith=selected_letter_name)

        if selected_letter_surname and selected_letter_surname!="Все":
            students_filter &= Q(user__middle_name__startswith=selected_letter_surname)

        students = Student.objects.filter(students_filter)



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


        return render(request, 'pivottable.html', context)





def lab_view(request):
    return render(request, 'labview.html')