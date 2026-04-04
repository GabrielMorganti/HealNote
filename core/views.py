import calendar

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView
from django.utils import timezone

from .forms import ConsultaForm, LembreteForm, MedicamentoForm, ReceitaForm, SignUpForm
from .models import Consulta, Lembrete, Medicamento, Receita
from .ocr import processar_receita


class SignUpView(CreateView):
	form_class = SignUpForm
	template_name = "registration/signup.html"
	success_url = reverse_lazy("login")


class DashboardView(LoginRequiredMixin, TemplateView):
	template_name = "core/home.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		today = timezone.localdate()
		calendar_obj = calendar.Calendar(firstweekday=6)
		meses = [
			"Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho",
			"Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro",
		]

		context["mes_atual"] = f"{meses[today.month - 1]} {today.year}"
		context["dias_semana"] = ["DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SAB"]
		context["calendario"] = calendar_obj.monthdayscalendar(today.year, today.month)
		context["dia_hoje"] = today.day
		
		# Limite removido da query para trazer todos os itens, 
		# mas o template fará o limite visual e rolagem, conforme solicitado.
		context["consultas"] = Consulta.objects.filter(usuario=self.request.user).order_by("data", "horario")
		context["medicamentos"] = Medicamento.objects.filter(usuario=self.request.user).order_by("horario")
		context["receitas"] = Receita.objects.filter(usuario=self.request.user)
		return context


class MedicamentoListView(LoginRequiredMixin, ListView):
	model = Medicamento

	def get_queryset(self):
		return Medicamento.objects.filter(usuario=self.request.user)


class MedicamentoCreateView(LoginRequiredMixin, CreateView):
	model = Medicamento
	form_class = MedicamentoForm
	success_url = reverse_lazy("medicamento_list")

	def form_valid(self, form):
		form.instance.usuario = self.request.user
		return super().form_valid(form)


class MedicamentoUpdateView(LoginRequiredMixin, UpdateView):
	model = Medicamento
	form_class = MedicamentoForm
	success_url = reverse_lazy("medicamento_list")

	def get_queryset(self):
		return Medicamento.objects.filter(usuario=self.request.user)


class MedicamentoDeleteView(LoginRequiredMixin, DeleteView):
	model = Medicamento
	success_url = reverse_lazy("medicamento_list")

	def get_queryset(self):
		return Medicamento.objects.filter(usuario=self.request.user)


class LembreteListView(LoginRequiredMixin, ListView):
	model = Lembrete

	def get_queryset(self):
		return Lembrete.objects.filter(medicamento__usuario=self.request.user)


class LembreteCreateView(LoginRequiredMixin, CreateView):
	model = Lembrete
	form_class = LembreteForm
	success_url = reverse_lazy("lembrete_list")

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields["medicamento"].queryset = Medicamento.objects.filter(usuario=self.request.user)
		return form


class LembreteUpdateView(LoginRequiredMixin, UpdateView):
	model = Lembrete
	form_class = LembreteForm
	success_url = reverse_lazy("lembrete_list")

	def get_queryset(self):
		return Lembrete.objects.filter(medicamento__usuario=self.request.user)

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields["medicamento"].queryset = Medicamento.objects.filter(usuario=self.request.user)
		return form


class LembreteDeleteView(LoginRequiredMixin, DeleteView):
	model = Lembrete
	success_url = reverse_lazy("lembrete_list")

	def get_queryset(self):
		return Lembrete.objects.filter(medicamento__usuario=self.request.user)


class ConsultaListView(LoginRequiredMixin, ListView):
	model = Consulta

	def get_queryset(self):
		return Consulta.objects.filter(usuario=self.request.user)


class ConsultaCreateView(LoginRequiredMixin, CreateView):
	model = Consulta
	form_class = ConsultaForm
	success_url = reverse_lazy("consulta_list")

	def form_valid(self, form):
		form.instance.usuario = self.request.user
		return super().form_valid(form)


class ConsultaUpdateView(LoginRequiredMixin, UpdateView):
	model = Consulta
	form_class = ConsultaForm
	success_url = reverse_lazy("consulta_list")

	def get_queryset(self):
		return Consulta.objects.filter(usuario=self.request.user)


class ConsultaDeleteView(LoginRequiredMixin, DeleteView):
	model = Consulta
	success_url = reverse_lazy("consulta_list")

	def get_queryset(self):
		return Consulta.objects.filter(usuario=self.request.user)


class ReceitaListView(LoginRequiredMixin, ListView):
	model = Receita

	def get_queryset(self):
		return Receita.objects.filter(usuario=self.request.user)


class ReceitaCreateView(LoginRequiredMixin, CreateView):
	model = Receita
	form_class = ReceitaForm
	success_url = reverse_lazy("receita_list")

	def form_valid(self, form):
		form.instance.usuario = self.request.user
		response = super().form_valid(form)
		self.object.texto_extraido = processar_receita(self.object.imagem.path)
		self.object.save(update_fields=["texto_extraido"])
		return response


class ReceitaDeleteView(LoginRequiredMixin, DeleteView):
	model = Receita
	success_url = reverse_lazy("receita_list")

	def get_queryset(self):
		return Receita.objects.filter(usuario=self.request.user)
