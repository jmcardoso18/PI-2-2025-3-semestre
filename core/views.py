import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Evento, Servico

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