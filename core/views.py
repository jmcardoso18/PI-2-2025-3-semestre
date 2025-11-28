import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Evento, Servico, Usuario
from .forms import ClienteForm
from .forms import ClienteForm, EventoForm

# -------------------------------------------------------------------
# API: Serviços (Para o Home do React)
# -------------------------------------------------------------------
def lista_servicos(request):
    servicos = Servico.objects.all().values('id', 'titulo', 'descricao', 'preco')
    return JsonResponse(list(servicos), safe=False)

# -------------------------------------------------------------------
# API: Login (Cria sessão para o Dashboard)
# -------------------------------------------------------------------
@csrf_exempt 
def login_react_session(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = authenticate(
                request, 
                username=data.get('username'), 
                password=data.get('password')
            )
            
            if user is not None:
                login(request, user) # Cria o cookie de sessão
                return JsonResponse({'message': 'Sucesso', 'redirect': '/dashboard/'})
            else:
                return JsonResponse({'error': 'Credenciais inválidas'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
            
    return JsonResponse({'error': 'Método não permitido'}, status=405)

# -------------------------------------------------------------------
# VIEW: Dashboard (Renderizado pelo Django)
# -------------------------------------------------------------------
@login_required(login_url='/admin/login/') 
def dashboard(request):
    # Tenta filtrar eventos pelo email do usuário logado para conectar
    # o User do Django Auth com o seu model Usuario personalizado
    try:
        eventos = Evento.objects.filter(usuario__email=request.user.email)
    except:
        # Fallback: Se não der para filtrar, retorna lista vazia ou todos (ajuste conforme necessidade)
        eventos = []

    context = {
        'usuario': request.user,
        'eventos': eventos
    }
    return render(request, 'core/dashboard.html', context)

# --- CRUD DE CLIENTES ---

@login_required(login_url='/admin/login/')
def cliente_lista(request):
    # Lista apenas quem é do tipo 'cliente'
    clientes = Usuario.objects.all() 
    return render(request, 'core/cliente_lista.html', {'clientes': clientes})

@login_required(login_url='/admin/login/')
def cliente_novo(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect('cliente_lista')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'core/cliente_form.html', {'form': form, 'titulo': 'Editar Cliente'})

@login_required(login_url='/admin/login/')
def cliente_deletar(request, id):
    cliente = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_lista')
    return render(request, 'core/cliente_confirmar_delete.html', {'cliente': cliente})

# --- CRUD DE EVENTOS ---

@login_required(login_url='/admin/login/')
def evento_lista(request):
    eventos = Evento.objects.all().order_by('data') # Ordenado por data
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
        form = EventoForm(instance=evento) # Preenche com os dados existentes
        
    return render(request, 'core/evento_form.html', {'form': form, 'titulo': 'Editar Evento'})

@login_required(login_url='/admin/login/')
def evento_deletar(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('evento_lista')
    # Reutiliza o template de confirmação de exclusão de cliente
    return render(request, 'core/cliente_confirmar_delete.html', {'objeto': evento.nome, 'tipo': 'Evento'})