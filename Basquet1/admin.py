from django.contrib import admin
from Basquet1.models import Entrenadores, Jugadores, Clubes, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Clubes)
admin.site.register(Entrenadores)
admin.site.register(Jugadores)
admin.site.register(Post, PostAdmin)








