from django.contrib import admin
from .models import Post, Comentario

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estatus','fecha_creado')
    list_filter = ("estatus",)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Post, PostAdmin)

@admin.register(Comentario)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contenido', 'post', 'fecha_creado', 'activo')
    list_filter = ('activo', 'fecha_creado')
    search_fields = ('nombre', 'email', 'contenido')
    actions = ['aprobar_comentarios']

    def aprobar_comentarios(self, request, queryset):
        queryset.update(active=True)
