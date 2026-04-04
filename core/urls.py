from django.urls import path

from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="home"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("medicamentos/", views.MedicamentoListView.as_view(), name="medicamento_list"),
    path("medicamentos/novo/", views.MedicamentoCreateView.as_view(), name="medicamento_create"),
    path("medicamentos/<int:pk>/editar/", views.MedicamentoUpdateView.as_view(), name="medicamento_update"),
    path("medicamentos/<int:pk>/excluir/", views.MedicamentoDeleteView.as_view(), name="medicamento_delete"),
    path("lembretes/", views.LembreteListView.as_view(), name="lembrete_list"),
    path("lembretes/novo/", views.LembreteCreateView.as_view(), name="lembrete_create"),
    path("lembretes/<int:pk>/editar/", views.LembreteUpdateView.as_view(), name="lembrete_update"),
    path("lembretes/<int:pk>/excluir/", views.LembreteDeleteView.as_view(), name="lembrete_delete"),
    path("consultas/", views.ConsultaListView.as_view(), name="consulta_list"),
    path("consultas/nova/", views.ConsultaCreateView.as_view(), name="consulta_create"),
    path("consultas/<int:pk>/editar/", views.ConsultaUpdateView.as_view(), name="consulta_update"),
    path("consultas/<int:pk>/excluir/", views.ConsultaDeleteView.as_view(), name="consulta_delete"),
    path("receitas/", views.ReceitaListView.as_view(), name="receita_list"),
    path("receitas/nova/", views.ReceitaCreateView.as_view(), name="receita_create"),
    path("receitas/<int:pk>/excluir/", views.ReceitaDeleteView.as_view(), name="receita_delete"),
]
