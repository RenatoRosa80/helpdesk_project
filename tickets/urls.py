from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.dashboard_user, name='user_dashboard'),
    path('create/', views.ticket_create, name='ticket_create'),
    path('ticket/<int:pk>/', views.ticket_detail, name='ticket_detail'),

    # admin
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/assign/<int:pk>/', views.assign_ticket, name='assign_ticket'),
]
