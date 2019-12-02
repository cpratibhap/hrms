from django.shortcuts import render
from .State import State
from .serializers import StateSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

#GET GET/{id} POST PUT PATCH DELETE
class StateOperations(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


def home():
    print("INSIDW VIEW")