from django.shortcuts import render

# Create your views here.
def home(request):   # acessar dados da página
     return render(request,'usuarios/home.html')    # acessar página html

def usuarios(request):
     pass
