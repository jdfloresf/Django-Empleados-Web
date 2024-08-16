from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView

from .forms import NewDepartamentoForm

from .models import Departamento
from apps.persona.models import Empleado

# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):

        depto = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname']
        )
        depto.save()

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre, 
            last_name = apellidos,
            job = '1',
            departamento = depto
        )

        return super(NewDepartamentoView, self).form_valid(form)