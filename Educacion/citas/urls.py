from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include



from . import views 
from .views import eliminar_cita

urlpatterns = [
    path('citas/', views.cita_list, name='listarcitas'),
    path('citacreate/', csrf_exempt(views.cita_create), name='citaCreate'),
    path ('eliminar_cita/<id>/',views.eliminar_cita,name="eliminar_cita"),
]