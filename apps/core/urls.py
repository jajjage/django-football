"""Core urls"""

from django.conf import settings
from django.urls import path, include

from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtailautocomplete.urls.admin import urlpatterns as \
    autocomplete_admin_urls

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/autocomplete/", include(autocomplete_admin_urls)),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),

    path("rosetta/", include("rosetta.urls")),

    path("account/", include("django.contrib.auth.urls")),

    path("", include("matches.urls", namespace='matches')),
    path("goals/", include("goals.urls", namespace='goals')),


    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url("pages/', include(wagtail_urls)),
]

if settings.DEBUG:
    # pylint: disable=C0412; ignore the ungrouped django imports
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    import debug_toolbar

    # Serve static and media files from development server
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
    # urlpatterns = staticfiles_urlpatterns() + urlpatterns
    # urlpatterns = static(
    #     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
