from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from items.views import ItemViewSet


router = DefaultRouter()
router.register(r'items', ItemViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="description!",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="Public License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('items.urls')),
    path('api/doc/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('', include(router.urls)),
]
