from django.shortcuts import render, get_object_or_404

from rest_framework import generics

from products.models import Celular

from products.serializers import CelularSerializer
  
def index(request):
    phone = Celular.objects.order_by("data_atualizacao").filter(publicada=True)

    return render(request, 'store/index.html', {'cards': phone})


class CelularListCreateView(generics.ListCreateAPIView):
    queryset = Celular.objects.all()
    serializer_class = CelularSerializer

class CelularRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Celular.objects.all()
    serializer_class = CelularSerializer
