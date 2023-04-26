"""IdentificationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from IdentitySystem.views import IdentityCardViewSet, PersonViewSet, AuthorityCardViewSet, RegionViewSet, \
    DepartmentViewSet, BoroughViewSet, DepartmentByRegionViewSet, BoroughByDepartmentViewSet, \
    IdentityCardByAuthorityViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'identity-cards', IdentityCardViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'authorities', AuthorityCardViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'boroughs', BoroughViewSet)
router.register(r'regions/(?P<region_id>\d+)/departments', DepartmentByRegionViewSet, basename='departments_by_region')
router.register(r'departments/(?P<department_id>\d+)/boroughs', BoroughByDepartmentViewSet, basename='borough_by_region'
                )
router.register(r'authorities/(?P<authority_id>\d+)/identity_cards', IdentityCardByAuthorityViewSet,
                basename='identity_card_by_authority')


schema_view = get_schema_view(
    openapi.Info(
        title="Système d'Identification",
        default_version='v1',
        description="Selon le model du Cameroun",
    ),
    public=True,
    permission_classes=[],
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
