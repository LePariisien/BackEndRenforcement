from rest_framework import serializers
from .models import Auteur, Editeur, Categorie, Livre, Exemplaire, Emprunt, Commentaire, Evaluation

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__' 

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class EditeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editeur
        fields = '__all__'

class LivreSerializer(serializers.ModelSerializer):
        auteur = AuteurSerializer(many=True, read_only=True)
        categorie = serializers.StringRelatedField()
        editeur = serializers.StringRelatedField()
        class Meta:
            model = Livre
            fields = '__all__'

class ExemplaireSerializer(serializers.ModelSerializer):
    livre = LivreSerializer()
    class Meta:
        model = Exemplaire
        fields = '__all__'


class EmpruntSerializer(serializers.ModelSerializer):
    utilisateur = serializers.StringRelatedField() 
    exemplaire = ExemplaireSerializer()  
    class Meta:
        model = Emprunt
        fields = '__all__'


class CommentaireSerializer(serializers.ModelSerializer):
    utilisateur = serializers.StringRelatedField() 
    livre = LivreSerializer() 
    class Meta:
        model = Commentaire
        fields = '__all__'

class EvaluationSerializer(serializers.ModelSerializer):
    utilisateur = serializers.StringRelatedField() 
    livre = LivreSerializer() 
    class Meta:
        model = Evaluation
        fields = '__all__'