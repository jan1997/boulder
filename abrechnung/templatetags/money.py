from django.contrib.humanize.templatetags.humanize import intcomma
from django import template

register = template.Library()


@register.filter(name='money')
def money(dollars):
    dollars = round(float(dollars), 2)
    return "%s%s€" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])