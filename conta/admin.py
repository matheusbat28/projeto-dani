from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'telefone', 'is_staff', )
    search_fields = ('username', 'email', 'first_name', 'last_name', 'telefone', )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('infomações Pessoais', {
            'fields': ('first_name', 'last_name', 'telefone','perfil_img' )
        }),
        ('Permissôes', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Datas Importantes', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
admin.site.register(Usuario, UsuarioAdmin)
