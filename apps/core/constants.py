from django.contrib.sites.models import Site

EMAIL_CONTEXT = {
    "site": Site.objects.first(),
}

