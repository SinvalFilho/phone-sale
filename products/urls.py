from django.urls import path
from .views import index, CelularListCreateView, CelularRetrieveUpdateDestroyView

urlpatterns = [
    path('', index, name='index'),
    path('celulares/', CelularListCreateView.as_view(), name='celular-list-create'),
    path('celulares/<int:pk>/', CelularRetrieveUpdateDestroyView.as_view(), name='celular-detail'),
]
