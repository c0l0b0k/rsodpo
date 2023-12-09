from django.shortcuts import render

from teacher.forms import *

def pivot_table_teacher(request):
    form = PivotTableForm()
    data = {
        'form': form
    }
    return render(request, 'pivottable.html', data)