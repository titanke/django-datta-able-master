from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),
  path('carrera/', views.carrera, name='carrera'),
  path('carrera/<int:car_id>/', views.detalle_car, name='carrera_det'),
  path('carrera/<int:car_id>/borrar', views.bor_car, name='carrera_bor'),
  path('carrera/crear/', views.crear_car, name='carrera_crear'),  
  path('estudiantes/', views.estudiantes, name='estudiantes'),
  path('cursos/', views.curso, name='cursos'),
  path('cursos/<int:curso_id>/', views.detalle_curso, name='cursos_det'),
  path('cursos/<int:curso_id>/cerrado', views.cer_curso, name='cursos_cer'),
  path('cursos/<int:curso_id>/borrar', views.bor_curso, name='cursos_bor'),
  path('cursos/crear/', views.crear_curso, name='cursos_crear'),

]
