from django.urls import path
from .views import login, cadastro, logout, AvaliacaoListCreateView, AvaliacaoRetrieveUpdateDestroyView

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('avaliacoes/', AvaliacaoListCreateView.as_view(), name='avaliacao-list-create'),
    path('avaliacoes/<int:pk>/', AvaliacaoRetrieveUpdateDestroyView.as_view(), name='avaliacao-detail'),
]
