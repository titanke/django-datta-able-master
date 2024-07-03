from django.shortcuts import render, redirect, get_object_or_404
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User 

from .models import *

@login_required
def index(request):

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)


def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)

@login_required
def carrera(request):
  context = {
  'carrera' : Carrera.objects.all(),
  'parent': 'universidad',
  'segment': 'carrera'
  }
  return render(request, "pages/carrera.html",context)

@login_required
def crear_car(request):
  if request.method == "GET":
      return render(request,"pages/crea_car.html",{
        "form": Carreraform
      })
  else:
    try:
      form = Carreraform(request.POST)
      print(request.POST)
      n_car = form.save(commit=False)
      n_car.user = request.user
      n_car.save()
      return redirect("carrera")
    except ValueError:
        return render(request,"pages/crea_car.html",{
            "form": Carreraform,
            "error": "Envia la informacion correcta",
            'parent': 'Carrera',
          },)

def detalle_car(request,car_id):
  if request.method=="GET":
      carrera = get_object_or_404(Carrera,pk=car_id)
      form =Carreraform(instance=carrera)
      return render(request, "pages/deta_car.html",{
        "carrera": carrera,
        "form": form,
        'parent': 'Carrera',
      })
  else:
    try:
      carrera = get_object_or_404(Carrera,pk=car_id)
      form =Carreraform(request.POST,instance=carrera)
      form.save()
      return redirect("carrera")
    except ValueError:
      return render(request, "pages/deta_car.html",{
        "curso": carrera,
        "form": form,
        "error":"error al actualizar carrera",
        'parent': 'Carrera',
      })      
  
def bor_car(request,car_id):
  carrera = get_object_or_404(Carrera,pk=car_id)
  if request.method == "POST":
    carrera.delete()
    return redirect("carrera")
   



def estudiantes(request):
  context = {
  'parent': 'universidad',
  'segment': 'estudiantes',
  'estudiantes' : User.objects.all(),
  }
  return render(request, "pages/estudiantes.html",context)





def curso(request):
  context = {
  'cursos' : Curso.objects.all(),
  'segment': 'cursos'
  }
  return render(request, "pages/curso.html",context)

def detalle_curso(request,curso_id):
  if request.method=="GET":
      curso = get_object_or_404(Curso,pk=curso_id)
      form =Cursoform(instance=curso)
      return render(request, "pages/deta_curso.html",{
        "curso": curso,
        "form": form
      })
  else:
    try:
      curso = get_object_or_404(Curso,pk=curso_id)
      form =Cursoform(request.POST,instance=curso)
      form.save()
      return redirect("cursos")
    except ValueError:
      return render(request, "pages/deta_curso.html",{
        "curso": curso,
        "form": form,
        "error":"error al actualizar curso"
      })      
  
def crear_curso(request):
  if request.method == "GET":
      return render(request,"pages/crea_cur.html",{
        "form": Cursoform
      })
  else:
    try:
      form = Cursoform(request.POST)
      print(request.POST)
      n_curso = form.save(commit=False)
      n_curso.user = request.user
      n_curso.save()
      return redirect("cursos")
    except ValueError:
        return render(request,"pages/crea_cur.html",{
            "form": Cursoform,
            "error": "Envia la informacion correcta"
          },)
      

def cer_curso(request,curso_id):
  curso = get_object_or_404(Curso,pk=curso_id)
  if request.method == "POST":
    curso.fechafin=timezone.now()
    curso.save()
    return redirect("cursos")
  

def bor_curso(request,curso_id):
  curso = get_object_or_404(Curso,pk=curso_id)
  if request.method == "POST":
    curso.delete()
    return redirect("cursos")
   

 
    