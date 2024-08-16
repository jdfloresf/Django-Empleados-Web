from django.urls import path
from . import views

app_name = 'persona_app'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('listar-empleados/', views.ListAllEmpledos.as_view(), name='empleados_all'),
    path('listar-by-area/<shorname>/', views.ListByArea.as_view(), name='empleados_area'),
    path('listar-empleados-admin/', views.ListaEmpledosAdmin.as_view(), name='empleados_admin'),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='add_empleado'),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
    path('buscar-empleado/', views.ListEmpleadoByKword.as_view()),
]
