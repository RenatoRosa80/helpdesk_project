# tickets/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse
from .models import Ticket, Category
from .forms import TicketForm

def home(request):
    if request.user.is_authenticated:
        return redirect('tickets:dashboard')
    else:
        return redirect('accounts:login')

@login_required
def dashboard(request):
    # Buscar todos os tickets do usuário
    user_tickets = Ticket.objects.filter(created_by=request.user)
    
    # Estatísticas
    total_tickets = user_tickets.count()
    open_tickets = user_tickets.filter(status='open').count()
    in_progress_tickets = user_tickets.filter(status='in_progress').count()
    closed_tickets = user_tickets.filter(status='closed').count()
    
    # Chamados recentes (últimos 5)
    recent_tickets = user_tickets.order_by('-created_at')[:5]
    
    context = {
        'total_tickets': total_tickets,
        'open_tickets': open_tickets,
        'in_progress_tickets': in_progress_tickets,
        'closed_tickets': closed_tickets,
        'recent_tickets': recent_tickets,
    }
    
    return render(request, "tickets/dashboard.html", context)

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(created_by=request.user)
    return render(request, "tickets/ticket_list.html", {"tickets": tickets})

@login_required
def ticket_create(request):
    if request.method == "POST":
        # Processar os dados do formulário
        title = request.POST.get("title")
        description = request.POST.get("description")
        category_id = request.POST.get("category")
        ticket_type = request.POST.get("ticket_type", "problem")
        code_snippet = request.POST.get("code_snippet", "")
        code_language = request.POST.get("code_language", "")
        
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                messages.error(request, "Categoria inválida.")
                categories = Category.objects.all()
                return render(request, "tickets/ticket_form.html", {"categories": categories})
        else:
            messages.error(request, "Selecione uma categoria.")
            categories = Category.objects.all()
            return render(request, "tickets/ticket_form.html", {"categories": categories})
        
        ticket = Ticket(
            title=title,
            description=description,
            category=category,
            ticket_type=ticket_type,
            code_snippet=code_snippet,
            code_language=code_language,
            created_by=request.user,
            status='open'
        )
        ticket.save()
        
        messages.success(request, "Chamado criado com sucesso!")
        return redirect("tickets:ticket_list")
    
    else:
        # GARANTIR que as categorias são passadas para o template
        categories = Category.objects.all()
        return render(request, "tickets/ticket_form.html", {"categories": categories})

@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, created_by=request.user)
    return render(request, "tickets/ticket_detail.html", {"ticket": ticket})

@login_required
def ticket_update(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, created_by=request.user)

    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, "Chamado atualizado!")
            return redirect("tickets:ticket_detail", ticket_id=ticket.id)
    else:
        form = TicketForm(instance=ticket)

    return render(request, "tickets/ticket_update.html", {"form": form, "ticket": ticket})

@login_required
def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, created_by=request.user)
    
    if request.method == "POST":
        ticket.delete()
        messages.success(request, "Chamado excluído com sucesso!")
        return redirect("tickets:ticket_list")
    
    return render(request, "tickets/ticket_confirm_delete.html", {"ticket": ticket})

@login_required
def ticket_close(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, created_by=request.user)
    
    if request.method == "POST":
        ticket.status = 'closed'
        ticket.save()
        messages.success(request, "Chamado fechado com sucesso!")
        return redirect("tickets:ticket_list")
    
    return render(request, "tickets/ticket_confirm_close.html", {"ticket": ticket})


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