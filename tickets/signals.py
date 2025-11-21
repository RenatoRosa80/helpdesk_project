from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Ticket, TicketHistory

@receiver(post_save, sender=Ticket)
def create_history_on_create(sender, instance, created, **kwargs):
    if created:
        TicketHistory.objects.create(
            ticket=instance,
            actor=instance.created_by,
            action='Chamado criado',
            to_status=instance.status,
            note=f'Categoria: {instance.get_category_display()}'
        )

@receiver(pre_save, sender=Ticket)
def create_history_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old = Ticket.objects.get(pk=instance.pk)
    except Ticket.DoesNotExist:
        return

    changes = []
    if old.status != instance.status:
        changes.append(f'Status: {old.get_status_display()} -> {instance.get_status_display()}')
    if old.assigned_to_id != instance.assigned_to_id:
        old_assignee = old.assigned_to.get_full_name() if old.assigned_to else 'Nenhum'
        new_assignee = instance.assigned_to.get_full_name() if instance.assigned_to else 'Nenhum'
        changes.append(f'Assignee: {old_assignee} -> {new_assignee}')
    if old.assigned_team != instance.assigned_team:
        changes.append(f'Team: {old.assigned_team} -> {instance.assigned_team}')

    if changes:
        TicketHistory.objects.create(
            ticket=instance,
            actor=None,  # você pode atualizar em views para passar request.user
            action='; '.join(changes),
            from_status=old.status,
            to_status=instance.status
        )
