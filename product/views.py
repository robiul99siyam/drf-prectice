from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Brand,Categroy,Product
from.serializer import BrandSerializer,CategroySerializer,ProductSerializer



class CategoryViewsets(viewsets.ModelViewSet):

    """ 
            use of model viewset . atuomacitce crud opation create 
    """

    queryset = Categroy.objects.all()
    serializer_class = CategroySerializer

    def create(self,request,*agrs,**kwargs):
        seriaizer  = self.get_serializer(data=request.data)
        if seriaizer.is_valid():
            seriaizer.save()
            return Response(seriaizer.data,status=status.HTTP_201_CREATED)
        return Response(seriaizer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,*args,**kwargs):
        instance = self.get_object()
        serializer =  self.get_serializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

 