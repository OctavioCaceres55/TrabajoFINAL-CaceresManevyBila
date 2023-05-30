from django.contrib import admin
from Basquet1.models import Entrenadores, Jugadores, Clubes, Articulo

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'fecha','autor')
    list_filter = ("titulo",)
    search_fields = ['titulo', 'contenido']

admin.site.register(Clubes)
admin.site.register(Entrenadores)
admin.site.register(Jugadores)
admin.site.register(Articulo, PostAdmin)












