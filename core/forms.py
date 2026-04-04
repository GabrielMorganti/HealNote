from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Consulta, Lembrete, Medicamento, Receita, User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ["nome", "dosagem", "horario", "frequencia", "observacoes"]
        widgets = {
            "horario": forms.TimeInput(attrs={"type": "time"}),
        }


class LembreteForm(forms.ModelForm):
    class Meta:
        model = Lembrete
        fields = ["medicamento", "horario", "ativo"]
        widgets = {
            "horario": forms.TimeInput(attrs={"type": "time"}),
        }


class ConsultaForm(forms.ModelForm):
    data = forms.DateField(
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
    )

    class Meta:
        model = Consulta
        fields = ["data", "horario", "descricao", "local", "latitude", "longitude"]
        widgets = {
            "horario": forms.TimeInput(attrs={"type": "time"}),
            "local": forms.TextInput(attrs={"placeholder": "Digite o endereco para localizar no mapa"}),
            "latitude": forms.HiddenInput(),
            "longitude": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.data:
            self.initial["data"] = self.instance.data.strftime("%Y-%m-%d")

    def clean(self):
        cleaned_data = super().clean()
        local = cleaned_data.get("local")
        latitude = cleaned_data.get("latitude")
        longitude = cleaned_data.get("longitude")

        if local and (latitude is None or longitude is None):
            raise ValidationError("Confirme o local no mapa para salvar latitude e longitude.")

        return cleaned_data


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ["imagem"]
