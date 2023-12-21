from django import template
from django.template.defaultfilters import stringfilter

from task.models import Topic

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

register = template.Library()

@register.simple_tag
def subsections(topic):
    subsections = Topic.objects.filter(subsection=topic.topic_id).order_by('topic_id')
    return subsections



