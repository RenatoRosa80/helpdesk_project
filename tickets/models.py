# tickets/models.py
from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} ({self.department})"

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Aberto'),
        ('in_progress', 'Em andamento'),
        ('closed', 'Fechado'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    assigned_to = models.ForeignKey(User, null=True, blank=True, related_name='assigned_tickets', on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.category and not self.department:
            self.department = self.category.department
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"#{self.id} - {self.title}"
    
    
    
# tickets/models.py
class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Aberto'),
        ('in_progress', 'Em andamento'),
        ('closed', 'Fechado'),
    ]
    
    TICKET_TYPES = [
        ('problem', 'Reportar Problema'),
        ('improvement', 'Sugerir Melhoria'),
        ('question', 'Dúvida'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    ticket_type = models.CharField(max_length=20, choices=TICKET_TYPES, default='problem')  # NOVO
    code_snippet = models.TextField(blank=True, null=True)  # NOVO CAMPO
    code_language = models.CharField(max_length=50, blank=True, null=True)  # NOVO CAMPO
    created_by = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    assigned_to = models.ForeignKey(User, null=True, blank=True, related_name='assigned_tickets', on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.category and not self.department:
            self.department = self.category.department
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"#{self.id} - {self.title}"
    
    
    
    