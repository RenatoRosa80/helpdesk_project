from django.contrib import admin
from django.urls import path, include
from tickets import views as ticket_views  # importa a home

urlpatterns = [
    path('admin/', admin.site.urls),

    # Inclui apps com namespace correto
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('tickets/', include(('tickets.urls', 'tickets'), namespace='tickets')),

    # Home do sistema
    path('', ticket_views.home, name='home'),
]



from django.urls import path
from . import views

app_name = "tickets"

urlpatterns = [
    path("", views.ticket_list, name="ticket_list"),
    path("create/", views.ticket_create, name="ticket_create"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("<int:ticket_id>/", views.ticket_detail, name="ticket_detail"),  # CORREÇÃO: sem 'detail/'
    path("<int:ticket_id>/update/", views.ticket_update, name="ticket_update"),
    path("<int:ticket_id>/delete/", views.ticket_delete, name="ticket_delete"),
    path("<int:ticket_id>/close/", views.ticket_close, name="ticket_close"),
]

