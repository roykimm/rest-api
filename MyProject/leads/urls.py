from django.urls import path, include
from rest_framework import routers
from .api import LeadViewSet, TodoViewSet

router = routers.DefaultRouter()
router.register('', LeadViewSet, 'leads')

router2 = routers.DefaultRouter()
router2.register('', TodoViewSet, 'todos')


urlpatterns = [
    path('api/leads/', include(router.urls)),
    path('api/todos/', include(router2.urls)),
]