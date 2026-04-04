from django.contrib import admin

from .models import Consulta, Historico, Lembrete, Medicamento, Receita, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ("username", "email", "is_staff")
	search_fields = ("username", "email")


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
	list_display = ("nome", "dosagem", "horario", "frequencia", "usuario")
	search_fields = ("nome", "usuario__username")
	list_filter = ("frequencia",)


@admin.register(Lembrete)
class LembreteAdmin(admin.ModelAdmin):
	list_display = ("medicamento", "horario", "ativo")
	list_filter = ("ativo",)


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
	list_display = ("usuario", "data", "horario", "local")
	search_fields = ("usuario__username", "local")


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
	list_display = ("usuario", "data_upload")
	readonly_fields = ("texto_extraido", "data_upload")


@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
	list_display = ("usuario", "data")
	readonly_fields = ("data",)
