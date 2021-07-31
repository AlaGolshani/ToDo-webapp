from datetime import timezone
from datetime import datetime
from django import template
from django.utils.timesince import timeuntil, timesince

register = template.Library()


@register.simple_tag
def time_diff(value):
    """
    This template tag measures the time difference between now and the given date or datetime
    """
    now = datetime.now(timezone.utc)

    try:
        if value > now:
            return timeuntil(value)
        elif value < now:  # expired
            return str(timesince(value, now)) + ' ago'
    except TypeError:
        return None  # the argument isn't valid
