from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

@register.filter(name='add_attrs')
def add_attrs(field, attrs):
    if not hasattr(field, 'as_widget'):
        return field
    attrs_dict = {}
    definitions = attrs.split(',')
    for definition in definitions:
        key, value = definition.split(':')
        attrs_dict[key.strip()] = value.strip()
    return field.as_widget(attrs=attrs_dict)