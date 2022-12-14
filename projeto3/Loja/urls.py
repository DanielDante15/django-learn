from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('avaliacoes',views.AvaliacaoViewSet,basename='avaliacoes')

# urlpatterns = router.urls
urlpatterns = [
    path('produtos/', views.ProdutoListar.as_view()),
    path('produtos/<int:pk>/', views.ProdutoDetalhe.as_view()),
    path('clientes/', views.cliente_listar),
    path('clientes/<int:id>/', views.cliente_detalhes),
    path('pedidos/', views.pedido_listar),
    path('pedidos/<int:id>/', views.pedido_detalhes),
    path('items_pedidos/', views.pedido_item_listar),
    path('items_pedidos/<int:id>/', views.pedido_item_detalhes),
    path('avaliacoes/', views.avaliacao_listar),   
]
