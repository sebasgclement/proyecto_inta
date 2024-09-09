from django.shortcuts import render
from rest_framework import generics
from .models import Pregunta
from .serializers import PreguntaSerializer


# Create your views here.
from rest_framework import viewsets
from .models import Usuario, Categoria, Pregunta
from .serializers import UsuarioSerializer, CategoriaSerializer, PreguntaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class PreguntasPorCategoriaAPIView(generics.ListAPIView):
    serializer_class = PreguntaSerializer

    def get_queryset(self):
        categoria_id = self.kwargs['categoria_id']
        print(f"Buscando preguntas para la categoría: {categoria_id}")
        preguntas = Pregunta.objects.filter(categoria=categoria_id)
        print(f"Número de preguntas encontradas: {preguntas.count()}")  # Para depuración
        return preguntas