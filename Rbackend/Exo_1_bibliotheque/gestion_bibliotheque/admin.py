from django.contrib import admin
from .models import Auteur, Editeur, Categorie, Livre, Exemplaire, Emprunt, Commentaire, Evaluation

admin.site.register(Auteur)
admin.site.register(Editeur)
admin.site.register(Categorie)
admin.site.register(Livre)
admin.site.register(Exemplaire)
admin.site.register(Emprunt)
admin.site.register(Commentaire)
admin.site.register(Evaluation)

