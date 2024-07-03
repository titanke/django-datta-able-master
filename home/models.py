from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Product(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100) 
    info  = models.CharField(max_length = 100, default = '')
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Carrera(models.Model):
    codigo = models.CharField(max_length=3,primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)
    def __str__(self):
        txt = "{0} duracion: {1} año(s)"
        return txt.format(self.nombre,self.duracion)

class Estu(models.Model):
    dni = models.CharField(max_length=3,primary_key=True)
    apeliidoP = models.CharField(max_length=35)
    apeliidoM = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    feNac = models.DateField()
    sexos=[
        ("F","Femenino"),
        ("M","Masculino")
    ]
    sexo = models.CharField(max_length=1,choices=sexos,default="F")
    carrera = models.ForeignKey(Carrera,null=False,blank=False,on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)
    def __str__(self):
        txt ="{0} {1},{2}"
        return txt.format(self.apeliidoP,self.apeliidoM,self.nombres)

class Curso(models.Model):
    codigo = models.CharField(max_length=6,primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)
    fechaini = models.DateTimeField(auto_now_add=True)
    fechafin = models.DateTimeField(null=True,blank=False)
    def __str__(self):
        txt ="{0} {1},{2}"
        return txt.format(self.codigo,self.nombre,self.creditos)
    
class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    #estudiante = models.ForeignKey(Estu,null=False,blank=False,on_delete=models.CASCADE)
    estudiante = models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,null=False,blank=False,on_delete=models.CASCADE)
    fechmat = models.DateField(auto_now_add=True)
    def __str__(self):
        txt ="{0} {1},{2}"
        return txt.format(self.id,self.estudiante,self.curso)


