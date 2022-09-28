from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estatus','fecha_creado')
    list_filter = ("estatus",)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Post, PostAdmin)

