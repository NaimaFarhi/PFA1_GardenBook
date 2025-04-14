from django.contrib import admin
from .models import (
    User,
    Livre,
    LivreEmprunte,
    Reservation,
    Evenement,
    Critique,
    Amende,
    Alerte
)

admin.site.register(User)
admin.site.register(Livre)
admin.site.register(LivreEmprunte)
admin.site.register(Reservation)
admin.site.register(Evenement)
admin.site.register(Critique)
admin.site.register(Amende)
admin.site.register(Alerte)
