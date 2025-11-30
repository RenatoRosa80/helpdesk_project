# tickets/forms.py
from django import forms
from .models import Ticket, Category

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título do chamado'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva o problema em detalhes'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'category': 'Categoria',
        }
        
        
# tickets/forms.py
from django import forms
from .models import Ticket, Category

class TicketForm(forms.ModelForm):
    # Opções de linguagens de programação
    LANGUAGE_CHOICES = [
        ('', 'Selecione a linguagem'),
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
        ('cpp', 'C++'),
        ('csharp', 'C#'),
        ('php', 'PHP'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('sql', 'SQL'),
        ('bash', 'Bash/Shell'),
        ('other', 'Outra'),
    ]
    
    code_language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'code-language'}),
        label="Linguagem do Código"
    )
    
    code_snippet = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 10,
            'placeholder': 'Cole seu código aqui...',
            'id': 'code-snippet'
        }),
        label="Código"
    )
    
    ticket_type = forms.ChoiceField(
        choices=Ticket.TICKET_TYPES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label="Tipo de Chamado",
        initial='problem'
    )

    class Meta:
        model = Ticket
        fields = ['ticket_type', 'title', 'description', 'code_snippet', 'code_language', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título do chamado'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva o problema ou melhoria em detalhes...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'category': 'Categoria',
        }