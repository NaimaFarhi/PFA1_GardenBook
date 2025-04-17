from django.db import models
from django.contrib.auth.models import AbstractUser

class RoleName(models.TextChoices):
    ADMIN = 'Administrator'
    BIBLIOTHECAIRE = "bibliothecaire"
    LECTEUR = "lecteur"
class GenreName(models.TextChoices):
   Children = "children"
   YA = "Young Adult"
   Adult = "Adult"

class MembershipStatus(models.TextChoices):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    SUSPENDED = 'Suspended'


class User(AbstractUser):
    cin = models.CharField(max_length=20, unique=True) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cin = models.CharField(max_length=20, unique=True, default=1) 
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=RoleName.choices)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, choices=MembershipStatus.choices, default=MembershipStatus.ACTIVE)

    def __str__(self):
        return self.username


class Livre(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    nom = models.CharField(max_length=255,default="")
    auteur = models.CharField(max_length=255,default="")
    dispo = models.BooleanField(default=True)
    pubDate = models.DateField(null=True, blank=True)
    nbPage = models.IntegerField(default="")
    language = models.CharField(max_length=244,default="")
    genres = models.CharField(max_length=244,default="")
    keywords = models.CharField(max_length=244,default="")
    description = models.CharField(max_length=244,default="")
    audience = models.CharField(max_length=20, choices=GenreName.choices, default="")


class LivreEmprunte(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt = models.DateField()
    date_limite_retour = models.DateField()
    retard = models.BooleanField(default=False)

class Reservation(models.Model):
    id_reservation = models.CharField(max_length=50, unique=True)
    lecteur = models.ForeignKey(User, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)

class Evenement(models.Model):
    type = models.CharField(max_length=100)
    date = models.DateField()
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)

class Critique(models.Model):
    id_crt = models.CharField(max_length=50, unique=True)
    notation = models.IntegerField()
    commentaire = models.TextField()
    lecteur = models.ForeignKey(User, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)

class Amende(models.Model):
    id_amende = models.CharField(max_length=50, unique=True)
    par_livre = models.FloatField()
    paye = models.BooleanField(default=False)
    livre_emprunte = models.ForeignKey(LivreEmprunte, on_delete=models.CASCADE)

class Alerte(models.Model):
    id_alerte = models.CharField(max_length=50, unique=True)
    lecteur = models.ForeignKey(User, on_delete=models.CASCADE)
