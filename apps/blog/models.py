"""wagtail page models"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, \
    FieldRowPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList


class StandardPage(Page):
    """A generic content page."""
    show_in_menus_default = True

    class Meta:
        """Meta"""
        verbose_name = _("Standard page")
        verbose_name_plural = _("Standard pages")

    body = RichTextField()
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('seo_title'),
            FieldPanel('show_in_menus'),
            FieldPanel('search_description'),
        ], _('Common page configuration')),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('go_live_at'),
                FieldPanel('expire_at'),
            ], classname="label-above"),
        ], _('Scheduled publishing'), classname='publishing')
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=_('Content')),
        ObjectList(promote_panels, heading=_('Settings'), classname="settings"),
    ])


class FormField(AbstractFormField):
    """Form field, used by contactpages"""
    page = ParentalKey(
        'ContactPage', on_delete=models.CASCADE, related_name='form_fields')

    def __str__(self):
        """name"""
        return self.label


class ContactPage(AbstractEmailForm):
    """
    A generic content page.
    """
    show_in_menus_default = True

    class Meta:
        """Meta info"""
        verbose_name = _("Contact page")
        verbose_name_plural = _("Contact pages")

    body = RichTextField()
    thank_you_text = RichTextField(blank=True, verbose_name=_('Thank you text'))
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    form_panels = [
        InlinePanel('form_fields', label="Form fields"),
    ]

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('seo_title'),
            FieldPanel('show_in_menus'),
            FieldPanel('search_description'),
        ], _('Common page configuration')),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('go_live_at'),
                FieldPanel('expire_at'),
            ], classname="label-above"),
        ], _('Scheduled publishing'), classname='publishing')
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=_('Content')),
        ObjectList(form_panels, heading=_('Form')),
        ObjectList(promote_panels, heading=_('Settings'), classname="settings"),
    ])


class HomePage(Page):
    """Custom page for homepage"""
