"""urls"""

from django.conf import settings
from django.urls import path, include

from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("rosetta/", include("rosetta.urls")),

    path("account/", include("django.contrib.auth.urls")),

    path("", include("matches.urls")),
    path("goals/", include("goals.urls")),
    path("api/", include("api.urls")),
    path("wagtail/", include("blog.urls")),
]

if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
