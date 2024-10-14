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
    editeur = serializers.PrimaryKeyRelatedField(queryset=Editeur.objects.all())
    categorie = serializers.PrimaryKeyRelatedField(queryset=Categorie.objects.all())
    auteurs = serializers.PrimaryKeyRelatedField(many=True, queryset=Auteur.objects.all())
    class Meta:
        model = Livre
        fields = '__all__'

    def create(self, validated_data):
        auteurs_data = validated_data.pop('auteurs') 
        livre = Livre.objects.create(**validated_data)
        livre.auteurs.set(auteurs_data) 
        return livre

    def update(self, instance, validated_data):
        auteurs_data = validated_data.pop('auteurs')
        instance.auteurs.set(auteurs_data) 
        return super().update(instance, validated_data)

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