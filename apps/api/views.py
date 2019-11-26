"""Schema view for API"""
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

SchemaView = get_schema_view(
    openapi.Info(
        title="Football API",
        default_version='v1',
        description="An API for retrieving information about matches played by DES Adamsnood 1",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)
