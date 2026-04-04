from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	pass


class Medicamento(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medicamentos")
	nome = models.CharField(max_length=255)
	dosagem = models.CharField(max_length=100)
	horario = models.TimeField()
	frequencia = models.CharField(max_length=100)
	observacoes = models.TextField(blank=True)

	class Meta:
		ordering = ["horario", "nome"]

	def __str__(self):
		return f"{self.nome} ({self.dosagem})"


class Lembrete(models.Model):
	medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name="lembretes")
	horario = models.TimeField()
	ativo = models.BooleanField(default=True)

	class Meta:
		ordering = ["horario"]

	def __str__(self):
		return f"{self.medicamento.nome} - {self.horario}"


class Consulta(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="consultas")
	data = models.DateField()
	horario = models.TimeField()
	descricao = models.TextField()
	local = models.CharField(max_length=255)
	latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
	longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

	class Meta:
		ordering = ["data", "horario"]

	def __str__(self):
		return f"{self.data} {self.horario} - {self.local}"


class Receita(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receitas")
	imagem = models.ImageField(upload_to="receitas/")
	texto_extraido = models.TextField(blank=True)
	data_upload = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-data_upload"]

	def __str__(self):
		return f"Receita de {self.usuario.username} em {self.data_upload:%d/%m/%Y}"


class Historico(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="historicos")
	descricao = models.TextField()
	data = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-data"]

	def __str__(self):
		return f"{self.usuario.username} - {self.data:%d/%m/%Y %H:%M}"
