import math
from mySite.models import Address, Contact, OpenHours, Logo, SocialMedia
from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings

register = template.Library()


@register.simple_tag()
def footer_content(key_value):
    c = Contact.objects.first()
    address = Address.objects.first()
    hrs = OpenHours.objects.all()

    context = {'contact': c,
               'address': address,
               'open_hours': hrs,
               'social': SocialMedia.objects.first()
               }
    return context[key_value]


@register.filter
def divide_and_roundup(value, arg):
    try:
        return math.ceil(int(value) / int(arg))
    except (ValueError, ZeroDivisionError):
        return None


@register.simple_tag()
def logo():
    l = Logo.objects.first()
    if l is not None:
        return l.logo.url
    else:
        return '#'


@register.simple_tag()
def favicon():
    l = Logo.objects.first()
    if l is not None:
        return l.favicon.url
    else:
        return '#'


def switch_lang_code(path, language):
    # Get the supported language codes
    lang_codes = [c for (c, name) in settings.LANGUAGES]

    # Validate the inputs
    if path == '':
        raise Exception('URL path for language switch is empty')
    elif path[0] != '/':
        raise Exception('URL path for language switch does not start with "/"')
    elif language not in lang_codes:
        raise Exception('%s is not a supported language code' % language)

    # Split the parts of the path
    parts = path.split('/')

    # Add or substitute the new language prefix
    if parts[1] in lang_codes:
        parts[1] = language
    else:
        parts[0] = "/" + language

    # Return the full new path
    return '/'.join(parts)


@register.filter
@stringfilter
def switch_i18n_prefix(path, language):
    """takes in a string path"""
    return switch_lang_code(path, language)


@register.filter
def switch_i18n(request, language):
    """takes in a request object and gets the path from it"""
    return switch_lang_code(request.get_full_path(), language)
