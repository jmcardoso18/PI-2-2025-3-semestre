import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# IMPORTS DOS SEUS MODELS E FORMS
from .models import Evento, Servico, Usuario, Atividade, Convidado, Tarefa, Fornecedor, Ocorrencia, Servico, Convidado
from .forms import ClienteForm, EquipeForm, EventoForm, FornecedorForm, TarefaForm, AtividadeForm, OcorrenciaForm, ServicoForm, ConvidadoForm

# --- FUNÇÕES AUXILIARES ---
def eh_admin(user):
    return user.is_staff

# -------------------------------------------------------------------
# API: Serviços (Para o Home do React)
# -------------------------------------------------------------------
def lista_servicos(request):
    servicos = Servico.objects.all().values('id', 'titulo', 'descricao', 'preco')
    return JsonResponse(list(servicos), safe=False)

# -------------------------------------------------------------------
# API: Login (Lógica Tripla de Redirecionamento)
# -------------------------------------------------------------------
@csrf_exempt 
def login_react_session(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # 1. ADMIN (Staff)
            if user.is_staff:
                return redirect('/dashboard/')
            
            # Tenta achar o perfil personalizado para decidir entre Cliente e Colaborador
            try:
                # Busca pelo email, já que definimos que o username é o email
                perfil = Usuario.objects.get(email=user.username)
                
                # 2. COLABORADOR (Se tiver "colaborador" ou "equipe" no tipo)
                if 'colaborador' in perfil.tipo.lower() or 'equipe' in perfil.tipo.lower():
                    return redirect('colaborador_home')
                
                # 3. CLIENTE (Padrão)
                else:
                    return redirect('/area-cliente/')
                    
            except Usuario.DoesNotExist:
                # Se não achar perfil mas logou, manda para área do cliente por segurança
                return redirect('/area-cliente/')
                
        else:
            return redirect('http://localhost:5173/login?error=invalid_credentials')
            
    return JsonResponse({'error': 'Método não permitido'}, status=405)

# -------------------------------------------------------------------
# VIEW: Dashboard Admin (Visão Geral / KPIs)
# -------------------------------------------------------------------
@login_required(login_url='/admin/login/') 
def dashboard(request):
    
    if not request.user.is_staff:
        try:
            # Busca o perfil pelo email
            perfil = Usuario.objects.get(email=request.user.email)
            
            if 'colaborador' in perfil.tipo.lower() or 'equipe' in perfil.tipo.lower():
                return redirect('colaborador_home')
            
            # Senão, Cliente -> Área do Cliente
            return redirect('area_cliente')
            
        except Usuario.DoesNotExist:
            return redirect('area_cliente')

    # --- LÓGICA DO ADMIN ---
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
@user_passes_test(eh_admin, login_url='/area-cliente/')
def cliente_lista(request):
    clientes = Usuario.objects.all() 
    return render(request, 'core/cliente_lista.html', {'clientes': clientes})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def cliente_novo(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            # Cria Login Django
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            nome = form.cleaned_data['nome']

            if not User.objects.filter(username=email).exists():
                User.objects.create_user(username=email, email=email, password=senha, first_name=nome.split()[0])
            else:
                user = User.objects.get(username=email)
                user.set_password(senha)
                user.save()
            return redirect('cliente_lista')
    else:
        form = ClienteForm()
    return render(request, 'core/cliente_form.html', {'form': form, 'titulo': 'Novo Cliente'})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def cliente_editar(request, id):
    cliente = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            # Atualiza senha
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
@user_passes_test(eh_admin, login_url='/area-cliente/')
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
@user_passes_test(eh_admin, login_url='/area-cliente/')
def evento_lista(request):
    eventos = Evento.objects.all().order_by('data')
    return render(request, 'core/evento_lista.html', {'eventos': eventos})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
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
@user_passes_test(eh_admin, login_url='/area-cliente/')
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
@user_passes_test(eh_admin, login_url='/area-cliente/')
def evento_deletar(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('evento_lista')
    return render(request, 'core/cliente_confirmar_delete.html', {'objeto': evento.nome, 'tipo': 'Evento'})

# -------------------------------------------------------------------
# CRUD DE FORNECEDORES
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def fornecedor_lista(request):
    fornecedores = Fornecedor.objects.all().order_by('empresa')
    return render(request, 'core/fornecedor_lista.html', {'fornecedores': fornecedores})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
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
@user_passes_test(eh_admin, login_url='/area-cliente/')
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
@user_passes_test(eh_admin, login_url='/area-cliente/')
def fornecedor_deletar(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('fornecedor_lista')
    return render(request, 'core/cliente_confirmar_delete.html', {'objeto': fornecedor.empresa, 'tipo': 'Fornecedor'})

# -------------------------------------------------------------------
# CRUD DE TAREFAS (PENDÊNCIAS)
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def tarefa_lista(request):
    tarefas = Tarefa.objects.all().order_by('data_limite')
    return render(request, 'core/tarefa_lista.html', {'tarefas': tarefas})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
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
@user_passes_test(eh_admin, login_url='/area-cliente/')
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
@user_passes_test(eh_admin, login_url='/area-cliente/')
def tarefa_deletar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefa_lista')
    return render(request, 'core/cliente_confirmar_delete.html', {'objeto': tarefa.titulo, 'tipo': 'Tarefa'})

# -------------------------------------------------------------------
# CRUD DE ACESSOS (EQUIPE)
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def equipe_lista(request):
    # Lista todos que NÃO são clientes/noivos (filtro simples)
    equipe = Usuario.objects.exclude(tipo__in=['Noiva', 'Noivo', 'Cliente']).order_by('nome')
    return render(request, 'core/equipe_lista.html', {'equipe': equipe})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def equipe_nova(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            # 1. Salva no banco personalizado
            membro = form.save()
            
            # 2. Cria o Login do Django com permissões
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            nome = form.cleaned_data['nome']
            tipo = form.cleaned_data['tipo']

            # Define se é Admin (Staff) com base no cargo
            eh_staff = (tipo == 'Cerimonialista')

            if not User.objects.filter(username=email).exists():
                User.objects.create_user(
                    username=email, 
                    email=email, 
                    password=senha, 
                    first_name=nome.split()[0],
                    is_staff=eh_staff # <--- AQUI ESTÁ O SEGREDINHO
                )
            else:
                u = User.objects.get(username=email)
                u.set_password(senha)
                u.is_staff = eh_staff
                u.save()

            return redirect('equipe_lista')
    else:
        form = EquipeForm()
    return render(request, 'core/equipe_form.html', {'form': form, 'titulo': 'Novo Membro da Equipe'})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def equipe_editar(request, id):
    membro = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=membro)
        if form.is_valid():
            form.save()
            # Atualiza login e permissão
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            tipo = form.cleaned_data['tipo']
            eh_staff = (tipo == 'Cerimonialista')
            
            try:
                u = User.objects.get(username=email)
                if senha: u.set_password(senha)
                u.is_staff = eh_staff
                u.save()
            except User.DoesNotExist:
                pass
                
            return redirect('equipe_lista')
    else:
        form = EquipeForm(instance=membro)
    return render(request, 'core/equipe_form.html', {'form': form, 'titulo': 'Editar Membro'})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def equipe_deletar(request, id):
    membro = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        try:
            u = User.objects.get(username=membro.email)
            u.delete() 
        except:
            pass
        membro.delete()
        return redirect('equipe_lista')
    return render(request, 'core/cliente_confirmar_delete.html', {'objeto': membro.nome, 'tipo': 'Membro da Equipe'})

# -------------------------------------------------------------------
# CRUD DE SERVIÇOS (PACOTES)
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def servico_lista(request):
    servicos = Servico.objects.all().order_by('preco')
    return render(request, 'core/servico_lista.html', {'servicos': servicos})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def servico_novo(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servico_lista')
    else:
        form = ServicoForm()
    return render(request, 'core/servico_form.html', {'form': form, 'titulo': 'Novo Serviço'})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def servico_editar(request, id):
    servico = get_object_or_404(Servico, id=id)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('servico_lista')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'core/servico_form.html', {'form': form, 'titulo': 'Editar Serviço'})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def servico_deletar(request, id):
    servico = get_object_or_404(Servico, id=id)
    if request.method == 'POST':
        servico.delete()
        return redirect('servico_lista')
    return render(request, 'core/cliente_confirmar_delete.html', {'objeto': servico.titulo, 'tipo': 'Serviço'})

# -------------------------------------------------------------------
# ÁREA DO COLABORADOR
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
def colaborador_home(request):
    eventos = Evento.objects.all().order_by('data')
    return render(request, 'core/colaborador_home.html', {'eventos': eventos})

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
# CRUD DE CONVIDADOS
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
def meus_convidados(request):
    # 1. Identifica o evento do cliente logado
    try:
        evento = Evento.objects.filter(usuario__email=request.user.email).first()
    except:
        return redirect('area_cliente')

    if not evento:
        return redirect('area_cliente')

    # 2. Processa o Formulário de Adição
    if request.method == 'POST':
        form = ConvidadoForm(request.POST)
        if form.is_valid():
            convidado = form.save(commit=False)
            convidado.evento = evento # Vincula automaticamente ao evento do cliente
            convidado.save()
            return redirect('meus_convidados')
    else:
        form = ConvidadoForm()

    # 3. Lista os convidados existentes
    convidados = evento.convidados.all().order_by('nome')
    
    # Cálculos rápidos
    total_confirmados = convidados.filter(status='Confirmado').count()
    total_pessoas = sum(c.acompanhantes + 1 for c in convidados) # Titular + Acompanhantes

    context = {
        'evento': evento,
        'convidados': convidados,
        'form': form,
        'total_confirmados': total_confirmados,
        'total_pessoas': total_pessoas
    }
    return render(request, 'core/meus_convidados.html', context)

# View para excluir (caso o cliente errou)
@login_required(login_url='/admin/login/')
def excluir_convidado(request, id):
    convidado = get_object_or_404(Convidado, id=id)
    # Segurança: Garante que o convidado pertence a um evento do usuário logado
    if convidado.evento.usuario.email == request.user.email:
        convidado.delete()
    return redirect('meus_convidados')

# -------------------------------------------------------------------
# CRUD DE ATIVIDADES (CRONOGRAMA)
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def atividade_lista(request):
    # Ordena por evento e depois por horário
    atividades = Atividade.objects.all().order_by('evento', 'horario')
    return render(request, 'core/atividade_lista.html', {'atividades': atividades})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def atividade_nova(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atividade_lista')
    else:
        form = AtividadeForm()
    return render(request, 'core/atividade_form.html', {'form': form, 'titulo': 'Nova Atividade'})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def atividade_editar(request, id):
    atividade = get_object_or_404(Atividade, id=id)
    if request.method == 'POST':
        form = AtividadeForm(request.POST, instance=atividade)
        if form.is_valid():
            form.save()
            return redirect('atividade_lista')
    else:
        form = AtividadeForm(instance=atividade)
    return render(request, 'core/atividade_form.html', {'form': form, 'titulo': 'Editar Atividade'})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def atividade_deletar(request, id):
    atividade = get_object_or_404(Atividade, id=id)
    if request.method == 'POST':
        atividade.delete()
        return redirect('atividade_lista')
    return render(request, 'core/cliente_confirmar_delete.html', {'objeto': atividade.nome, 'tipo': 'Atividade'})

# -------------------------------------------------------------------
# CRUD DE OCORRÊNCIAS
# -------------------------------------------------------------------

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def ocorrencia_lista(request):
    ocorrencias = Ocorrencia.objects.all().order_by('-id') # Mais recentes primeiro
    return render(request, 'core/ocorrencia_lista.html', {'ocorrencias': ocorrencias})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def ocorrencia_nova(request):
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ocorrencia_lista')
    else:
        form = OcorrenciaForm()
    return render(request, 'core/ocorrencia_form.html', {'form': form, 'titulo': 'Registrar Ocorrência'})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def ocorrencia_editar(request, id):
    ocorrencia = get_object_or_404(Ocorrencia, id=id)
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, instance=ocorrencia)
        if form.is_valid():
            form.save()
            return redirect('ocorrencia_lista')
    else:
        form = OcorrenciaForm(instance=ocorrencia)
    return render(request, 'core/ocorrencia_form.html', {'form': form, 'titulo': 'Editar Ocorrência'})

@login_required(login_url='/admin/login/')
@user_passes_test(eh_admin, login_url='/area-cliente/')
def ocorrencia_deletar(request, id):
    ocorrencia = get_object_or_404(Ocorrencia, id=id)
    if request.method == 'POST':
        ocorrencia.delete()
        return redirect('ocorrencia_lista')
    return render(request, 'core/cliente_confirmar_delete.html', {'objeto': ocorrencia.tipo, 'tipo': 'Ocorrência'})

# -------------------------------------------------------------------
# LOGOUT
# -------------------------------------------------------------------
def logout_react(request):
    logout(request)
    return redirect('http://localhost:5173/login')