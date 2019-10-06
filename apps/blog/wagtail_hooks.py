"""Wagtail admin customization"""

from django.utils.html import format_html
from django.contrib.staticfiles.templatetags.staticfiles import static

from wagtail.core import hooks


@hooks.register('insert_global_admin_js')
def global_admin_js():
    """Add custom javascript"""
    return format_html(
        '<script src="{}"></script>', static('js/admin/global.js'))


@hooks.register('insert_global_admin_css')
def global_admin_css():
    """Add custom css"""
    return format_html(
        '<link rel="stylesheet" href="{}">', static('css/admin/global.css'))
