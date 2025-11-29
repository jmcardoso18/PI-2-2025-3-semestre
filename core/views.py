import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# IMPORTS DOS SEUS MODELS E FORMS
from .models import Evento, Servico, Usuario, Atividade, Convidado, Tarefa, Fornecedor
from .forms import ClienteForm, EventoForm, FornecedorForm, TarefaForm

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
        # Lendo dados de Formulário (request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user) # Cria o cookie de sessão
            
            # LÓGICA DE REDIRECIONAMENTO
            if user.is_staff:
                return redirect('/dashboard/')     # Admin
            else:
                return redirect('/area-cliente/')  # Cliente
        else:
            # Erro: Manda de volta para o React com aviso
            return redirect('http://127.0.0.1:5173/login?error=true')
            
    return JsonResponse({'error': 'Método não permitido'}, status=405)

# -------------------------------------------------------------------
# VIEW: Dashboard Admin
# -------------------------------------------------------------------
@login_required(login_url='/admin/login/') 
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
            # 1. Salva o cliente
            cliente = form.save()
            
            # 2. Cria/Atualiza o Login do Django
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
                if senha:
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
    evento = Evento.objects.filter(usuario__email=request.user.email).first()

    if not evento:
        if request.user.is_staff:
            evento = Evento.objects.first()
        
        if not evento:
            # CORREÇÃO: Enviando o usuário no contexto para o nome aparecer no topo
            return render(request, 'core/cliente_area.html', {'evento': None, 'usuario': request.user})

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
# CRUD DE FORNECEDORES
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
def fornecedor_lista(request):
    fornecedores = Fornecedor.objects.all().order_by('empresa')
    return render(request, 'core/fornecedor_lista.html', {'fornecedores': fornecedores})

@login_required(login_url='/admin/login/')
def fornecedor_novo(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedor_lista')
    else:
        form = FornecedorForm()
    return render(request, 'core/fornecedor_form.html', {'form': form, 'titulo': 'Novo Fornecedor'})

@login_required(login_url='/admin/login/')
def fornecedor_editar(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('fornecedor_lista')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'core/fornecedor_form.html', {'form': form, 'titulo': 'Editar Fornecedor'})

@login_required(login_url='/admin/login/')
def fornecedor_deletar(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('fornecedor_lista')
    # Reutiliza o template genérico de exclusão
    return render(request, 'core/cliente_confirmar_delete.html', {'objeto': fornecedor.empresa, 'tipo': 'Fornecedor'})


# -------------------------------------------------------------------
# CRUD DE TAREFAS (PENDÊNCIAS)
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
def tarefa_lista(request):
    tarefas = Tarefa.objects.all().order_by('data_limite')
    return render(request, 'core/tarefa_lista.html', {'tarefas': tarefas})

@login_required(login_url='/admin/login/')
def tarefa_nova(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefa_lista')
    else:
        form = TarefaForm()
    return render(request, 'core/tarefa_form.html', {'form': form, 'titulo': 'Nova Tarefa'})

@login_required(login_url='/admin/login/')
def tarefa_editar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefa_lista')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'core/tarefa_form.html', {'form': form, 'titulo': 'Editar Tarefa'})

@login_required(login_url='/admin/login/')
def tarefa_deletar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefa_lista')
    return render(request, 'core/cliente_confirmar_delete.html', {'objeto': tarefa.titulo, 'tipo': 'Tarefa'})

# -------------------------------------------------------------------
# LOGOUT
# -------------------------------------------------------------------
def logout_react(request):
    logout(request)
    return redirect('http://localhost:5173/login')