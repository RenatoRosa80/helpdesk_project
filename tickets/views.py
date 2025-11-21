from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Ticket, TicketHistory, Team
from .forms import TicketCreateForm, TicketAssignForm

@login_required
def dashboard_user(request):
    # lista de chamados do usuário
    tickets = Ticket.objects.filter(created_by=request.user).order_by('-created_at')
    return render(request, 'tickets/user_dashboard.html', {'tickets': tickets})

@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketCreateForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            messages.success(request, 'Chamado criado com sucesso.')
            return redirect('tickets:user_dashboard')
    else:
        form = TicketCreateForm()
    return render(request, 'tickets/ticket_create.html', {'form': form})

@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    history = ticket.history.all()
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket, 'history': history})

# função helper para checar se o user pertence a staff (pode personalizar)
def is_staff_user(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff_user)
def admin_dashboard(request):
    # visão administrativa: pode filtrar por times
    tickets = Ticket.objects.all().order_by('-created_at')
    teams = Team.choices
    return render(request, 'tickets/admin_dashboard.html', {'tickets': tickets, 'teams': teams})

@login_required
@user_passes_test(is_staff_user)
def assign_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketAssignForm(request.POST, instance=ticket)
        if form.is_valid():
            t = form.save(commit=False)
            # marca actor na história manualmente:
            old_assignee = ticket.assigned_to
            t.save()
            # criar histórico explícito associando actor
            TicketHistory.objects.create(
                ticket=t,
                actor=request.user,
                action=f'Chamado atualizado por {request.user.get_full_name() or request.user.username}',
                from_status=ticket.status,
                to_status=t.status,
                note=f'Alterado por {request.user.username}'
            )
            messages.success(request, 'Chamado atualizado.')
            return redirect('tickets:admin_dashboard')
    else:
        form = TicketAssignForm(instance=ticket)
    return render(request, 'tickets/assign_ticket.html', {'form': form, 'ticket': ticket})
