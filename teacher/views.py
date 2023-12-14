from django.shortcuts import render

from teacher.forms import *


def pivot_table_teacher(request):
    # Получаем преподавателя для текущего пользователя
    teacher = Teacher.objects.get(user=request.user)

    # Получаем все группы, связанные с этим преподавателем
    teacher_groups = teacher.groups.all()

    # Передаем только эти группы в форму
    form = PivotTableForm(groups=teacher_groups)

    data = {
        'user': request.user,
        'form': form,
    }

    return render(request, 'pivottable.html', data)