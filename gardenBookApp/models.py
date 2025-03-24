from django.db import models
from django.contrib.auth.models import AbstractUser

class RoleName(models.TextChoices):
    ADMIN = "admin"
    LECTEUR = "lecteur"

class User(AbstractUser):
        groups = models.ManyToManyField(
        "auth.Group",
        related_name="User_groups",
        blank=True
    )
        user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="User_permissions",
        blank=True
    )

        role = models.CharField(max_length=20, choices=RoleName.choices)

class Livre(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    nom = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    stock = models.IntegerField()

class Lecteur(User):
    pass

class Bibliothecaire(User):
    pass

class LivreEmprunte(models.Model):
    lecteur = models.ForeignKey(Lecteur, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt = models.DateField()
    date_limite_retour = models.DateField()
    retard = models.BooleanField(default=False)

class Reservation(models.Model):
    id_reservation = models.CharField(max_length=50, unique=True)
    lecteur = models.ForeignKey(Lecteur, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)

class Evenement(models.Model):
    type = models.CharField(max_length=100)
    date = models.DateField()
    responsable = models.ForeignKey(Bibliothecaire, on_delete=models.CASCADE)

class Critique(models.Model):
    id_crt = models.CharField(max_length=50, unique=True)
    notation = models.IntegerField()
    commentaire = models.TextField()
    lecteur = models.ForeignKey(Lecteur, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)

class Amende(models.Model):
    id_amende = models.CharField(max_length=50, unique=True)
    par_livre = models.FloatField()
    paye = models.BooleanField(default=False)
    livre_emprunte = models.ForeignKey(LivreEmprunte, on_delete=models.CASCADE)

class Alerte(models.Model):
    id_alerte = models.CharField(max_length=50, unique=True)
    lecteur = models.ForeignKey(Lecteur, on_delete=models.CASCADE)
