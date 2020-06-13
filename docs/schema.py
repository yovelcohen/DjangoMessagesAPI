from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Messages API",
        default_version='v1',
        description="Simple messages API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="yovell04@gmail.ocm"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
