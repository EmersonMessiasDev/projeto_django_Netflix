from pyexpat import model
from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView,ListView , DetailView

# Create your views here.

class Homepage(TemplateView):
    template_name = "homepage.html"

class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    #? object_views -> Lista de itens do modelo
    
class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    #? object -> lista um filme 
    
    
    
    
    
    
# FUNCTION BASE VIEWS
# url - view - html
# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context["lista_filmes"] = lista_filmes
#     return render(request, "homefilmes.html", context) 
    

# def homepage(request):
#     return render(request, "homepage.html")