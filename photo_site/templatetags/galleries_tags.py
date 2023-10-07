from django import template

register = template.Library()

@register.filter(name="indexmarker")
def indexmarker_format(list, count):
    print(list[0][count])
    return list[0][count].image.url
