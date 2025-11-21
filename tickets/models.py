from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


User = settings.AUTH_USER_MODEL

class Team(models.TextChoices):
    DEVELOPERS = 'DEV', 'Desenvolvedores'
    DB = 'DB', 'Gerenciamento de Banco de Dados'
    SERVICE = 'CS', 'Service Customer'
    MANAGEMENT = 'MG', 'Gerenciamento Geral'

class Category(models.TextChoices):
    TECHNICAL = 'TECH', 'Fixar problemas técnicos'
    DATABASE = 'DB', 'Problemas relacionados ao DB'
    NEW_FEATURE = 'FEATURE', 'Nova solicitação para desenvolver'
    REMOVE_FEATURE = 'REMOVE', 'Remover funcionalidade'
    ACCESS = 'ACCESS', 'Problemas de acesso'

class Status(models.TextChoices):
    OPEN = 'OPEN', 'Aberto'
    IN_PROGRESS = 'IN_PROGRESS', 'Em andamento'
    PENDING = 'PENDING', 'Pendente'
    RESOLVED = 'RESOLVED', 'Resolvido'
    CLOSED = 'CLOSED', 'Fechado'

class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=Category.choices)
    created_by = models.ForeignKey(User, related_name='created_tickets', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    assigned_to = models.ForeignKey(User, related_name='assigned_tickets', null=True, blank=True, on_delete=models.SET_NULL)
    assigned_team = models.CharField(max_length=10, choices=Team.choices, null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    priority = models.IntegerField(default=3)  # 1 high, 3 normal, 5 low
    # opcional: attachments, logs, tags...
    def __str__(self):
        return f'#{self.pk} {self.title} ({self.get_status_display()})'

class TicketHistory(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='history', on_delete=models.CASCADE)
    actor = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=200)  # Ex: "Criou o chamado", "Alterou status", "Reencaminhou"
    from_status = models.CharField(max_length=20, choices=Status.choices, null=True, blank=True)
    to_status = models.CharField(max_length=20, choices=Status.choices, null=True, blank=True)
    note = models.TextField(blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.timestamp} - {self.action}'
