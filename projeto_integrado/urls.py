from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('accounts/',include("django.contrib.auth.urls")),
    path('estoque/', include('estoque.urls'), name='estoque'),
    path ('', TemplateView.as_view(template_name='home.html'), name='home'),
    
]
