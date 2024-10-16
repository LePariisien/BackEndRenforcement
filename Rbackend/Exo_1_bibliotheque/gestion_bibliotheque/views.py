from rest_framework import viewsets
from .pagination import LivrePagination, EmpruntPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Auteur, Editeur, Categorie, Livre, Exemplaire, Emprunt, Commentaire, Evaluation
from .serializers import AuteurSerializer, EditeurSerializer, CategorieSerializer, LivreSerializer, ExemplaireSerializer, EmpruntSerializer, CommentaireSerializer, EvaluationSerializer

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all() 
    serializer_class = AuteurSerializer

class EditeurViewSet(viewsets.ModelViewSet):
    queryset = Editeur.objects.all()
    serializer_class = EditeurSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['categorie', 'authors']
    ordering_fields = ['publication_date', 'title', 'page_number']
    pagination_class = LivrePagination
class ExemplaireViewSet(viewsets.ModelViewSet):
    queryset = Exemplaire.objects.all()
    serializer_class = ExemplaireSerializer

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['users', 'state', 'loan_date', 'expected_return_date']
    ordering_fields = ['loan_date', 'expected_return_date', 'state']
    pagination_class = EmpruntPagination

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer