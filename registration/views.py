from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template.loader import render_to_string
import subprocess
import os

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def success(request):
    # Pegar a última inscrição baseada na data mais recente
    latest_inscription = Registration.objects.latest('registration_date')
    context = {
        'latest_inscription': latest_inscription
    }
    return render(request, 'registration/success.html', context)

def generate_pdf(request):
    # Pegar a última inscrição
    latest_inscription = Registration.objects.latest('registration_date')
    
    # Renderizar o conteúdo LaTeX
    latex_content = render_to_string('registration/comprovativo.tex', {
        'logo_path': '/static/logo.jpg',  # Ajuste o caminho conforme necessário
        'name': latest_inscription.name,
        'registration_date': latest_inscription.registration_date.strftime('%d/%m/%Y %H:%M')
    })

    # Salvar o arquivo LaTeX temporário
    latex_file = '/tmp/comprovativo.tex'
    with open(latex_file, 'w') as f:
        f.write(latex_content)

    # Gerar o PDF usando latexmk
    pdf_file = '/tmp/comprovativo.pdf'
    subprocess.run(['latexmk', '-pdf', latex_file], check=True)

    # Ler o PDF gerado
    with open(pdf_file, 'rb') as f:
        pdf_content = f.read()

    # Remover arquivos temporários
    os.remove(latex_file)
    os.remove(pdf_file.replace('.pdf', '.aux'))
    os.remove(pdf_file.replace('.pdf', '.log'))
    os.remove(pdf_file.replace('.pdf', '.out'))

    # Retornar o PDF como resposta de download
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="comprovativo_{latest_inscription.name}.pdf"'
    return response

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:  # Apenas usuários com is_staff=True
            login(request, user)
            return redirect('admin_panel')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, 'registration/admin_login.html')

@login_required
def admin_panel(request):
    inscriptions = Registration.objects.all().order_by('-registration_date')
    if request.method == 'POST':
        inscription_id = request.POST.get('inscription_id')
        new_status = request.POST.get('status')
        if inscription_id and new_status in ['Pendente', 'Confirmada']:
            inscription = Registration.objects.get(id=inscription_id)
            inscription.status = new_status
            inscription.save()
            messages.success(request, f"Status da inscrição {inscription.name} alterado para {new_status}.")
    return render(request, 'registration/admin_panel.html', {'inscriptions': inscriptions})