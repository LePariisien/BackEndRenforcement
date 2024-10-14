from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from gestion_bibliotheque.views import AuteurViewSet, EditeurViewSet, CategorieViewSet, LivreViewSet, ExemplaireViewSet, EmpruntViewSet, CommentaireViewSet, EvaluationViewSet

router = routers.DefaultRouter()
router.register(r'auteurs', AuteurViewSet)
router.register(r'editeurs', EditeurViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'livres', LivreViewSet)
router.register(r'exemplaires', ExemplaireViewSet)
router.register(r'emprunts', EmpruntViewSet)
router.register(r'commentaires', CommentaireViewSet)
router.register(r'evaluations', EvaluationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
