from django.forms import widgets
from django.utils.safestring import mark_safe
from django.forms.widgets import ClearableFileInput
from django.conf import settings


class CustomPictureImageFieldWidget(widgets.FileInput):

    def render(self, name, value, attrs=None, renderer=None):
        default_html = super().render(name, value, attrs, renderer=renderer)
        img_html = ''
        if value and hasattr(value, 'url'):
            img_html = mark_safe(f'<img src="{value.url}" width="200" />')
        return mark_safe(f'{img_html}{default_html}')