from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('tickets/', include(('tickets.urls', 'tickets'), namespace='tickets')),
    path('', TemplateView.as_view(template_name='tickets/home.html'), name='home'),
]
