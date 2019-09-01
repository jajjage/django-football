"""Wagtail admin customization"""

from django.utils.html import format_html
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import escape

from wagtail.core import hooks


@hooks.register('insert_global_admin_js')
def global_admin_js():
    """Custom javascript"""
    return format_html(
        '<script src="{}"></script>', static('js/admin/global.js'))


@hooks.register('insert_global_admin_css')
def global_admin_css():
    """Custom css"""
    return format_html(
        '<link rel="stylesheet" href="{}">', static('css/admin/global.css'))


def external_link_handler(attrs):
    href = attrs["href"]
    return '<a href="%s" target="_blank" rel="nofollow noopener">' % escape(href)


@hooks.register('register_rich_text_features')
def register_external_link(features):
    features.register_link_type('external', external_link_handler)
