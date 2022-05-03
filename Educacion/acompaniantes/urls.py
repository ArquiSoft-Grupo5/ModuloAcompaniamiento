from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

from . import views

urlpatterns = [
    path('acompaniantes/', views.acompaniante_list, name='acompanianteList'),
    path('acompaniante/<id>', views.single_acompaniante, name='singleAcompaniante'),
    path('acompaniantecreate/', csrf_exempt(views.acompaniante_create), name='acompanianteCreate'),
]
