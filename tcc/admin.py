from django.contrib import admin

# Register your models here.

from .models import Paciente, Medico, Recepcionista, Consulta, Receita, Exames, Medicamento, Login, Agenda, TipoExame

admin.site.register(Paciente)

admin.site.register(Medico)

admin.site.register(Recepcionista)

admin.site.register(Consulta)

admin.site.register(Receita)

admin.site.register(Exames)

admin.site.register(Medicamento)

admin.site.register(Login)

admin.site.register(Agenda)

admin.site.register(TipoExame)


