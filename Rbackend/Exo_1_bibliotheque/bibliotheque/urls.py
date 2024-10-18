from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from gestion_bibliotheque.loginViews import LoginWithOTPView
from gestion_bibliotheque.OTPview import SetupOTPView
# from two_factor.urls import urlpatterns as tf_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Bibliothèque API",
        default_version='v1',
        description="Documentation de l'API de gestion de bibliothèque",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion_bibliotheque.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginWithOTPView.as_view(), name='login_with_otp'),
    path('setup-otp/', SetupOTPView.as_view(), name='setup_otp'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('2fa/', include('two_factor.urls', 'two_factor')),

]
