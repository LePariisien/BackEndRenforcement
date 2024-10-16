from django.db import models
from django.contrib.auth.models import User

class Auteur(models.Model):
    name = models.CharField(max_length=255)
    biographie = models.TextField()
    birthday = models.DateField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Editeur(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.URLField()
    mail_contact = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Categorie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Livre(models.Model):
    title = models.CharField(max_length=255)
    resume = models.TextField()
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    page_number = models.IntegerField()
    language = models.CharField(max_length=50)
    editors = models.ForeignKey(Editeur, on_delete=models.CASCADE, related_name='livres')
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name='livres')
    authors = models.ManyToManyField(Auteur, related_name='livres')

    def __str__(self):
        return self.title


class Exemplaire(models.Model):
    book = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='exemplaires')
    state = models.CharField(max_length=100)  # Ex : Neuf, Bon, Acceptable
    acquisition_date = models.DateField()
    localisation = models.CharField(max_length=255)  # Ex : Rayonnage A1
    disponibility = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book.title} - {self.localisation}"
    
class Emprunt(models.Model):
    STATUT_CHOICES = [
        ('in_progess', 'In progress'),
        ('complete', 'Complete'),
        ('late', '  Late'),
    ]

    copy = models.ForeignKey(Exemplaire, on_delete=models.CASCADE, related_name='emprunts')
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emprunts')
    loan_date = models.DateTimeField(auto_now_add=True)
    expected_return_date = models.DateField()
    effective_return_date = models.DateField(null=True, blank=True)
    state = models.CharField(max_length=20, choices=STATUT_CHOICES, default='in_progress')
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Emprunt de {self.copy} par {self.users.username}"
    
class Commentaire(models.Model):
    book = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='commentaires')
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentaires')
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    evaluation = models.IntegerField(default=0)  # Sur 5
    visible = models.BooleanField(default=True)
    modere = models.BooleanField(default=False)

    def __str__(self):
        return f"Commentaire de {self.users.username} sur {self.book.title}"
    
class Evaluation(models.Model):
    book = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='evaluations')
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='evaluations')
    evaluation = models.IntegerField()  # De 1 à 5
    commentary = models.TextField(null=True, blank=True)
    evaluation_date = models.DateTimeField(auto_now_add=True)
    recommended = models.BooleanField(default=False)
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Évaluation de {self.users.username} pour {self.book.title}"



