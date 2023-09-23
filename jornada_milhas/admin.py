from django.contrib import admin
from jornada_milhas.models import Depoimento


class Depoimentos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'depoimento', 'foto')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Depoimento, Depoimentos)
