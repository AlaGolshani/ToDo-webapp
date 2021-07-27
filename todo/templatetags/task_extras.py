from datetime import timezone
from django import template
from django.template.defaultfilters import stringfilter
from datetime import datetime

register = template.Library()


@register.filter
@stringfilter
def title(value):
    return value.title()


@register.simple_tag
def remaining_time(expiry_time):
    now = datetime.now(timezone.utc)
    if expiry_time > now:
        time_difference = str(expiry_time - now).split('.')[0]
        return time_difference
    else:
        return 0
