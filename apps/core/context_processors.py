""" Context processors """

from django.conf import settings
from wagtail.core.models import Site


def project(request):
    """ Puts the footer text in every context because it's variable. """

    context = {
        "project_name": settings.PROJECT_NAME,
        "project_url": settings.PROJECT_URL,
    }
    return context