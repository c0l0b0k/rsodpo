from django import template
from django.utils.html import format_html, format_html_join

from task.models import Task

register = template.Library()

from django.urls import reverse
from urllib.parse import urlencode

@register.simple_tag
def render_grouped_tasks(topic, grouped_tasks):
    if topic in grouped_tasks:
        tasks = grouped_tasks[topic]
        task_ids = [task.task_id for task in tasks]
        params = {'task_list': ','.join(map(str, task_ids))}

        task_links = format_html_join(
            '', '<li><a href="{}">Задача {}</a></li>',
            ((reverse('task_view', kwargs={'number': task.task_id}) + '?' + urlencode(params), idx + 1) for idx, task in
             enumerate(tasks))
        )
        return format_html('<ul>{}</ul>', task_links)
    else:
        return ''

@register.simple_tag
def link_tasks(list_task):
    tasks = Task.objects.filter(pk__in=list_task)
    print("-------------")
    print(tasks)
    print("-------------")
    task_ids = list_task
    print("++++++++++")
    print(task_ids)
    print("++++++++++")
    params = {'task_list': ','.join(map(str, task_ids))}
    task_links = format_html_join(
        '', '<a  class="btn btn-outline-primary" href="{}">Задача {}</a></li>',
        ((reverse('task_view', kwargs={'number': task.task_id}) + '?' + urlencode(params), idx + 1) for idx, task in
         enumerate(tasks))
    )
    print(task_links)
    return format_html('{}', task_links)
