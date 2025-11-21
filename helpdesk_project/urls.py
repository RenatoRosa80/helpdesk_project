from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>HelpDesk - Página Inicial</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('tickets/', include('tickets.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
