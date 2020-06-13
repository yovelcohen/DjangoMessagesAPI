from django.urls import path

from .schema import schema_view

urlpatterns = [
    # Return a swagger docs in a json format.
    path('api/docs_json',
         schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    # API docs using the swagger UI.
    path('api/docs',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]
