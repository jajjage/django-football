"""constants"""
from django.contrib.sites.models import Site

SITE_CONTEXT = {
    'site': Site.objects.first(),
}
