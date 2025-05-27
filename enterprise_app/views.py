from django.shortcuts import render
import datetime
# Create your views here.
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import Material, Client, Shoes, Production
from .serializer import (
    MaterialSerializer, ClientSerializer, 
    ShoesSerializer, ProductionSerializer
)
from rest_framework.permissions import IsAuthenticated


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def toggle_isremoved(self, request, pk=None):
        try:
            material = self.get_object()
        except Material.DoesNotExist:
            return Response({'error': 'Material no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        material.isremoved = not material.isremoved
        material.save()
        serializer = self.get_serializer(material)
        return Response({'isremoved updated to:' f"{material.isremoved}"},status=status.HTTP_200_OK)

 

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [IsAuthenticated]



class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.select_related('material')
    serializer_class = ShoesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['color', 'material']
    search_fields = ['code', 'name','color']
    ordering_fields = ['code', 'name', 'color']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        material = serializer.validated_data['material']
        if material.isremoved:
            return Response({'material_id':'this material has been removed'},status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProductionViewSet(viewsets.ModelViewSet):
    """ViewSet para gestión de lotes productivos"""
    queryset = Production.objects.select_related(
        'shoes', 'client'
    )
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
    serializer_class = ProductionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tag', 'shoes', 'client', 'finished']
    search_fields = ['tag', 'shoes__name', 'shoes__code', 'client__name']
    ordering_fields = ['tag', 'create_at', 'shoes_ammount']
    ordering = ['tag', 'shoes', 'client', 'finished']
 

    @action(detail=True, methods=['patch'])
    def toggle_complete(self, request, pk=None):
        production = self.get_object()
        production.finished = not production.finished
        production.date_finished = datetime.datetime.now()
        production.save()
        serializer = self.get_serializer(production)
        return Response(serializer.data)

