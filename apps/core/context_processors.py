""" Context processors """
from .constants import SITE_CONTEXT


def project(request):
    """Adds site/project specific context to templates"""

    context = SITE_CONTEXT

    return context
