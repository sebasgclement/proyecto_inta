from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CategoriaViewSet, PreguntaViewSet, PreguntasPorCategoriaAPIView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'preguntas', PreguntaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('preguntas/categoria/<int:categoria_id>/', PreguntasPorCategoriaAPIView.as_view(), name='preguntas_por_categoria'),
    
]
