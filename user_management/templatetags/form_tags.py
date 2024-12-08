from django import template
from django.forms import Textarea

register = template.Library()

# @register.filter(name='add_class')
# def add_class(field, css_class):
#     return field.as_widget(attrs={"class": css_class})

@register.filter(name='add_class')
def add_class(field, css_class):
    if not hasattr(field, 'as_widget'):
        return field
    return field.as_widget(attrs={"class": css_class})

# @register.filter(name='add_attrs')
# def add_attrs(field, attrs):
#     if not hasattr(field, 'as_widget'):
#         return field
#     attrs_dict = {}
#     definitions = attrs.split(',')
#     for definition in definitions:
#         key, value = definition.split(':')
#         attrs_dict[key.strip()] = value.strip()
#     return field.as_widget(attrs=attrs_dict)

@register.filter(name='add_attrs')
def add_attrs(field, attrs):
    if not hasattr(field, 'as_widget'):
        return field
    attrs_dict = {}
    definitions = attrs.split(',')
    for definition in definitions:
        key, value = definition.split(':')
        attrs_dict[key.strip()] = value.strip()
    if 'type' in attrs_dict and attrs_dict['type'] == 'textarea':
        # del attrs_dict['type']
        return field.as_widget(widget=Textarea(attrs=attrs_dict))
    return field.as_widget(attrs=attrs_dict)