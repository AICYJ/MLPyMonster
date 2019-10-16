from django.shortcuts import render
from .serializers import PorkerSerializer
from .models import Porker
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Create your views here.


class ProkerViewSet(viewsets.ModelViewSet):
    queryset = Porker.objects.all()
    serializer_class = PorkerSerializer
