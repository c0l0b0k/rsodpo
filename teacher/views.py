from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from teacher.forms import *

@csrf_exempt
def pivot_table_teacher(request):
    topics = Topic.objects.filter(subsection=None)
    if request.method == 'GET':
        # Получаем преподавателя для текущего пользователя
        teacher = Teacher.objects.get(user=request.user)

        # Получаем все группы, связанные с этим преподавателем
        teacher_groups = teacher.groups.all()
        # if request.method == 'POST':
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


        print("-----")
        print(form.data)
        collapsed_nodes=form.data["collapsed_nodes"]
        if collapsed_nodes:
            # Преобразование строки в список целых чисел
            collapsed_nodes = list(map(int, collapsed_nodes.split(',')))
        else:
            # Если строка пуста, создаем пустой список
            collapsed_nodes = []
        data = {
            'user': request.user,
            'form': form,
            'topics': topics,
            'alphabet': 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ',
            'collapsed_nodes':collapsed_nodes
        }
        return render(request, 'pivottable.html', data)