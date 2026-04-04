from datetime import timedelta

from django.utils import timezone

from .models import Lembrete


def verificar_lembretes(janela_minutos=1):
    agora = timezone.localtime()
    inicio = agora - timedelta(minutes=janela_minutos)

    lembretes = Lembrete.objects.filter(
        ativo=True,
        horario__hour=agora.hour,
        horario__minute=agora.minute,
    ).select_related("medicamento")

    mensagens = []
    for lembrete in lembretes:
        mensagens.append(f"Hora do remedio: {lembrete.medicamento.nome}")

    return {
        "periodo": (inicio.time(), agora.time()),
        "mensagens": mensagens,
    }
