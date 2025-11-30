from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.models import Group
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group, _ = Group.objects.get_or_create(name='Clientes')
            user.groups.add(group)
            login(request, user)
            return redirect('tickets:my_tickets')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def user_login(request):
    if request.user.is_authenticated:
        return redirect('tickets:dashboard')
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}!")
            return redirect("tickets:dashboard")
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    
    return render(request, "accounts/login.html")

@csrf_exempt
def user_logout(request):
    """
    View de logout simplificada que aceita GET
    """
    logout(request)
    messages.success(request, "Você saiu do sistema com sucesso!")
    return redirect('accounts:login')

def register(request):
    if request.user.is_authenticated:
        return redirect('tickets:dashboard')
    return render(request, "accounts/register.html")

@user_passes_test(lambda u: u.is_superuser)
def admin_user_list(request):
    users = User.objects.all()
    return render(request, "accounts/admin_user_list.html", {"users": users})

@user_passes_test(lambda u: u.is_superuser)
def admin_user_edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "accounts/admin_user_edit.html", {"user": user})

@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    messages.success(request, "Usuário excluído com sucesso!")
    return redirect("accounts:admin_user_list")

def admin_user_create(request):
    return HttpResponse("admin_user_create - Página em desenvolvimento")

# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    print("🔐 LOGIN VIEW CHAMADA")  # Debug
    if request.user.is_authenticated:
        return redirect('tickets:dashboard')
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(f"📝 Tentando login: {username}")  # Debug

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}!")
            return redirect("tickets:dashboard")
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    
    return render(request, "accounts/login.html")

def user_logout(request):
    print("🚪 LOGOUT VIEW CHAMADA")  # Debug
    logout(request)
    messages.success(request, "Você saiu do sistema com sucesso!")
    return redirect('accounts:login')

def register(request):
    return render(request, "accounts/register.html")