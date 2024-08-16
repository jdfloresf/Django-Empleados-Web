from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import (
    ListView, 
    TemplateView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

class InicioView(TemplateView):
    """Vista que carga la pagina de inicio"""
    template_name = 'inicio.html'


class ListAllEmpledos(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        kw = self.request.GET.get("empleado", "")
        queryset = Empleado.objects.filter(
            first_name__icontains=kw
        )
        return queryset
    
class ListaEmpledosAdmin(ListView):
    model = Empleado
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'


class ListByArea(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        queryset = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return queryset

class ListEmpleadoByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        kw = self.request.GET.get("empleado", "")
        queryset = Empleado.objects.filter(
            first_name=kw
        )
        return queryset
    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        return context
    
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=4)
        return empleado.habilidades.all()
    
class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')
    
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

    

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)



class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')