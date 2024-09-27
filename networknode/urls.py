from rest_framework.routers import DefaultRouter
from django.urls import path, include
from networknode.views import NetworkNodeViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'network-nodes', NetworkNodeViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
