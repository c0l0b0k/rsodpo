from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

register = template.Library()

@register.filter(name='highlight_code')
@stringfilter
def highlight_code(value, language='python'):
    lexer = get_lexer_by_name(language, stripall=True)
    formatter = HtmlFormatter(linenos='table', cssclass='code')
    return mark_safe(highlight(value, lexer, formatter))