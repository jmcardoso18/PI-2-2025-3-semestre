import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# IMPORTS DOS SEUS MODELS E FORMS
from .models import Evento, Servico, Usuario, Atividade, Convidado, Tarefa
from .forms import ClienteForm, EventoForm

# -------------------------------------------------------------------
# API: Serviços (Para o Home do React)
# -------------------------------------------------------------------
def lista_servicos(request):
    servicos = Servico.objects.all().values('id', 'titulo', 'descricao', 'preco')
    return JsonResponse(list(servicos), safe=False)

# -------------------------------------------------------------------
# API: Login (Cria sessão e decide para onde redirecionar)
# -------------------------------------------------------------------

@csrf_exempt
def login_react_session(request):
    if request.method == 'POST':
        # MUDANÇA: Lê dados de formulário, não JSON
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Sucesso: Django redireciona o navegador para o painel correto
            if user.is_staff:
                return redirect('/dashboard/')
            else:
                return redirect('/area-cliente/')
        else:
            # Erro: Django manda de volta para o React com aviso
            return redirect('http://127.0.0.1:5173/login?error=true')
            
    return JsonResponse({'error': 'Método não permitido'}, status=405)

# -------------------------------------------------------------------
# VIEW: Dashboard Admin (Visão Geral / KPIs)
# -------------------------------------------------------------------
@login_required
def dashboard(request):
    if not request.user.is_staff:
        return redirect('area_cliente')

    todos_eventos = Evento.objects.all().order_by('data')
    total_clientes = Usuario.objects.all().count() 

    context = {
        'usuario': request.user,
        'total_eventos': todos_eventos.count(),
        'total_clientes': total_clientes,
        'proximos_eventos': todos_eventos[:5], 
        'eventos': todos_eventos 
    }
    return render(request, 'core/dashboard.html', context)

# -------------------------------------------------------------------
# CRUD DE CLIENTES
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
def cliente_lista(request):
    clientes = Usuario.objects.all() 
    return render(request, 'core/cliente_lista.html', {'clientes': clientes})

@login_required(login_url='/admin/login/')
def cliente_novo(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            # 1. Salva no banco personalizado
            cliente = form.save()
            
            # 2. Cria Login Django (Sincronização)
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            nome = form.cleaned_data['nome']

            if not User.objects.filter(username=email).exists():
                User.objects.create_user(
                    username=email, 
                    email=email, 
                    password=senha, 
                    first_name=nome.split()[0]
                )
            else:
                user = User.objects.get(username=email)
                user.set_password(senha)
                user.save()

            return redirect('cliente_lista')
    else:
        form = ClienteForm()
    return render(request, 'core/cliente_form.html', {'form': form, 'titulo': 'Novo Cliente'})

@login_required(login_url='/admin/login/')
def cliente_editar(request, id):
    cliente = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            # Atualiza senha do login se necessário
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            try:
                user_login = User.objects.get(username=email)
                if senha and not user_login.check_password(senha):
                    user_login.set_password(senha)
                    user_login.save()
            except User.DoesNotExist:
                pass
            return redirect('cliente_lista')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'core/cliente_form.html', {'form': form, 'titulo': 'Editar Cliente'})

@login_required(login_url='/admin/login/')
def cliente_deletar(request, id):
    cliente = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        try:
            # Tenta apagar o login também para manter limpo
            u = User.objects.get(username=cliente.email)
            u.delete()
        except:
            pass
        cliente.delete()
        return redirect('cliente_lista')
    return render(request, 'core/cliente_confirmar_delete.html', {'cliente': cliente})

# -------------------------------------------------------------------
# CRUD DE EVENTOS
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
def evento_lista(request):
    eventos = Evento.objects.all().order_by('data')
    return render(request, 'core/evento_lista.html', {'eventos': eventos})

@login_required(login_url='/admin/login/')
def evento_novo(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento_lista')
    else:
        form = EventoForm()
    return render(request, 'core/evento_form.html', {'form': form, 'titulo': 'Novo Evento'})

@login_required(login_url='/admin/login/')
def evento_editar(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('evento_lista')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'core/evento_form.html', {'form': form, 'titulo': 'Editar Evento'})

@login_required(login_url='/admin/login/')
def evento_deletar(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('evento_lista')
    return render(request, 'core/cliente_confirmar_delete.html', {'objeto': evento.nome, 'tipo': 'Evento'})

# -------------------------------------------------------------------
# ÁREA DO COLABORADOR
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
def colaborador_area(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    atividades = evento.atividades.all()
    convidados = evento.convidados.all()

    context = { 'evento': evento, 'atividades': atividades, 'convidados': convidados }
    return render(request, 'core/colaborador_area.html', context)

@csrf_exempt
def toggle_atividade(request, id):
    if request.method == 'POST':
        atividade = get_object_or_404(Atividade, id=id)
        atividade.feito = not atividade.feito
        atividade.save()
        return JsonResponse({'status': 'sucesso', 'feito': atividade.feito})
    return JsonResponse({'error': 'Método inválido'}, status=400)

# -------------------------------------------------------------------
# ÁREA DO CLIENTE
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
def area_cliente(request):
    # Busca o evento pelo email do usuário logado
    evento = Evento.objects.filter(usuario__email=request.user.email).first()

    if not evento:
        # Fallback para Admin testar: pega o primeiro evento
        if request.user.is_staff:
            evento = Evento.objects.first()
        
        if not evento:
            # Caso não tenha nenhum evento no sistema
            return render(request, 'core/base_dashboard.html', {'error': 'Nenhum evento encontrado.'})

    tarefas = evento.tarefas.all().order_by('data_limite')
    fornecedores = evento.fornecedores.all()
    atividades = evento.atividades.all().order_by('horario')

    context = {
        'evento': evento,
        'tarefas': tarefas,
        'fornecedores': fornecedores,
        'atividades': atividades,
        'usuario': request.user
    }
    return render(request, 'core/cliente_area.html', context)
    
@csrf_exempt
def toggle_tarefa(request, id):
    if request.method == 'POST':
        tarefa = get_object_or_404(Tarefa, id=id)
        tarefa.feito = not tarefa.feito
        tarefa.save()
        return JsonResponse({'status': 'sucesso', 'feito': tarefa.feito})
    return JsonResponse({'error': 'Erro'}, status=400)

# -------------------------------------------------------------------
# LOGOUT
# -------------------------------------------------------------------
def logout_react(request):
    logout(request) # Encerra sessão no Django
    return redirect('http://localhost:5173/login')