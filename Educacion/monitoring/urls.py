from django.contrib import admin
from django.urls import include, path, url 
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('', include('citas.urls')),
    path('', include('acompaniantes.urls')),
    url (r'^$', login,{'template_name': 'index.html'}, name='login')  
]

