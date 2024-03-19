from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from app.views import GetALLBooks,SearchAPI
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Gutenberg",
      default_version='v1',
      description="Gutenberg",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="pratappatilmh24@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('GetALLBooks/',GetALLBooks.as_view(),name="GetALLBooks"),
    path('SearchAPI/',SearchAPI.as_view(),name="SearchAPI"),
]