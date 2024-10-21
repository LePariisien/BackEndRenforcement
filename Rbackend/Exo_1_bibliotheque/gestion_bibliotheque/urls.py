from django.urls import path
from rest_framework.routers import DefaultRouter
from gestion_bibliotheque.views import AuteurViewSet, EditeurViewSet, CategorieViewSet, LivreViewSet, ExemplaireViewSet, EmpruntViewSet, CommentaireViewSet, EvaluationViewSet
from gestion_bibliotheque.loginViews import LoginWithOTPView
from gestion_bibliotheque.OTPview import SetupOTPView

router = DefaultRouter()

router.register(r'auteurs', AuteurViewSet)

router.register(r'editeurs', EditeurViewSet)

router.register(r'categories', CategorieViewSet)

router.register(r'livres', LivreViewSet)

router.register(r'exemplaires', ExemplaireViewSet)

router.register(r'emprunts', EmpruntViewSet)

router.register(r'commentaires', CommentaireViewSet)

router.register(r'evaluations', EvaluationViewSet)

urlpatterns = [
    path('login/', LoginWithOTPView.as_view(), name='login_with_otp'),
    path('setup-otp/', SetupOTPView.as_view(), name='setup_otp'),
]

urlpatterns += router.urls