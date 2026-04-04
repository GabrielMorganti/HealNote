# HealNote

Projeto de Pratica Profissional em ADS. Titulo: HealNote

## Integrantes

- GABRIEL MORGANTI SANTELO FERREIRA - 10441215
- JOSE FELLIPE - 10433493
- KAIKY IRINEU BITENCOURT - 10433497
- SEYEDEHZAHRA MOUSAVI - 10441352
- MATHEUS CARVALHO FERNANDES - 10443067

## Como testar o app (passo a passo)

### 1. Pre-requisitos

- Python 3.11+ instalado
- Git (opcional)
- Tesseract OCR instalado no sistema (necessario para OCR de receitas)

No Windows, instale o Tesseract e adicione o caminho do executavel ao PATH.

### 2. Abrir o projeto

No terminal, entre na pasta do projeto:

```powershell
cd "c:\Users\Admin\OneDrive - SENAC - SP\Área de Trabalho\Faculdade\Prat Prof\projeto\health_system"
```

### 3. Criar e ativar ambiente virtual

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear scripts, execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 4. Instalar dependencias

```powershell
pip install -r requirements.txt
```

### 5. Aplicar migracoes do banco

```powershell
python manage.py migrate
```

### 6. Criar usuario administrador (opcional, recomendado)

```powershell
python manage.py createsuperuser
```

### 7. Rodar o servidor

```powershell
python manage.py runserver
```

Acesse no navegador:

- http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

### 8. Testar funcionalidades principais

1. Cadastro e login de usuario.
2. Cadastro de medicamentos.
3. Cadastro de consultas e verificacao da listagem.
4. Cadastro de lembretes e exclusao/edicao.
5. Upload de receita para testar OCR.

Observacao sobre OCR:

- Se o Tesseract nao estiver instalado/configurado, o sistema exibira a mensagem de OCR indisponivel.

### 9. Rodar testes automatizados

```powershell
python manage.py test
```

Se tudo estiver correto, os testes serao executados sem erros.
