from django.shortcuts import render
from django.views.generic import TemplateView, ListView

class IndexView(TemplateView):
    template_name = 'home/home.html'


class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['A', 'B', 'C', 'D']
    context_object_name = 'lista_prueba'

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class HomeTemplate1View(TemplateView):
    template_name = "home/home1.html"

class HomeTemplate2View(TemplateView):
    template_name = "home/home2.html"

class HomeTemplate3View(TemplateView):
    template_name = "home/home3.html"
