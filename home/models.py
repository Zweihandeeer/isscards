from django.db import models
from django.shortcuts import render
# Create your models here.

class Cartas(models.Model):
    idbiblioteca = models.IntegerField(primary_key=True, verbose_name="IDBIBLIOTECA")
    juego = models.CharField(max_length=50, default="Juego", verbose_name="JUEGO")
    sets = models.CharField(max_length=50, default="Set", verbose_name="SET")
    idcarta = models.IntegerField(default = 0, verbose_name="IDCARTA")
    nombrecarta = models.CharField(max_length=50, default="Nombre Carta", verbose_name="NOMBRECARTA")    
    habilidad = models.CharField(max_length=250, default="Habilidad", verbose_name="HABILIDAD")
    keyword = models.CharField(max_length=50, default="Keyword", verbose_name="KEYWORD")    
    costomana = models.IntegerField(default = 0, verbose_name="COSTOMANA")
    fuerza = models.IntegerField( default = 0, verbose_name="FUERZA")    
    salud = models.IntegerField(default = 0, verbose_name="SALUD")
    rareza = models.CharField(max_length=50, default="Rareza", verbose_name="RAREZA")    
    tipocarta = models.CharField(max_length=50, default="Tipo carta", verbose_name="TIPOCARTA")
    region = models.CharField(max_length=50, default="Region", verbose_name="REGION")
    tipohechizo = models.CharField(max_length=50, default="Tipo hechizo", verbose_name="TIPOHECHIZO")
    
    def __str__(self):
        text = "({0}) {1} {2} ({3}) {4} {5} {6} {7} ({8}) ({9}) ({10}) {11} {12} {13}"
        return text.format(self.idbiblioteca, self.juego, self.set, self.idcarta, self.nombrecarta, self.habilidad, self.keyword, self.costomana, self.fuerza, self.salud, self.rareza, self.tipocarta, self.region, self.tipohechizo)