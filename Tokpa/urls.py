from django.urls import include, path
from django.contrib import admin

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from product.viewsets import ProductViewSet, ProductCategoryViewSet
from order.viewsets import OrderViewSet
from user.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'product_category', ProductCategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('admin/', admin.site.urls)
]
