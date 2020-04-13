from django.contrib import admin
from .models import *


admin.site.register(TipoUsuario)
admin.site.register(Disciplina)
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Horario)

