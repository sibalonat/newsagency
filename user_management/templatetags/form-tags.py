from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

# @register.filter(name='add_attrs')
# def add_attrs(field, css_class):
#     attrs = {}
#     definitions = css_class.split(',')
#     for definition in definitions:
#         key, value = definition.split(':')
#         attrs[key.strip()] = value.strip()
#     return field.as_widget(attrs=attrs)