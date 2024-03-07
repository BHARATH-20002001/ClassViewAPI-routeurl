from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from app.models import *
from rest_framework.response import Response
from app.serializers import *

class ProductCrud(ViewSet):
    def list(self,request):
        LPO = Product.objects.all()
        JPO = ProdectModelSerializer(LPO,many=True)
        return Response(JPO.data)
    

    def retrieve(self,request,pk):
        PO = Product.objects.get(pk=pk)
        JPO = ProdectModelSerializer(PO)
        return Response(JPO.data)
    
    def create(self,request):
        JD = request.data
        PDO = ProdectModelSerializer(data=JD)
        if PDO.is_valid():
            PDO.save()
        return Response({'created':'data created'})
    

    def update(self,request,pk):
        PO = Product.objects.get(pk=pk)
        JD = request.data
        PDO = ProdectModelSerializer(PO,data=JD)
        if PDO.is_valid():
            PDO.save()
            return Response({'created':'data created'})
        else:
            return Response({'error':'data not inserted'})

    def partial_update(self,request,pk):
        PO = Product.objects.get(pk=pk)
        JD = request.data
        PDO = ProdectModelSerializer(PO,data=JD,partial=True)
        if PDO.is_valid():
            PDO.save()
            return Response({'created':'data created'})
        else:
            return Response({'error':'data not inserted'})
        

    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'deleted':'Data is deleted'})
