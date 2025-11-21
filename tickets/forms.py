from django import forms
from .models import Ticket

class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'category', 'priority']
        widgets = {
            'description': forms.Textarea(attrs={'rows':4}),
        }

class TicketAssignForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['assigned_to', 'assigned_team', 'status', 'priority']
