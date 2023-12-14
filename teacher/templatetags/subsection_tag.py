from django import template
from task.models import Topic

register = template.Library()

@register.simple_tag
def subsections(topic):
    subsections = Topic.objects.filter(subsection=topic.topic_id)
    return subsections