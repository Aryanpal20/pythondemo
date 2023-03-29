from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from .serializers import ItemSerializers
from .models import Item
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ItemPost(APIView):
    def post(self, request):
        item = ItemSerializers(data=request.data)
        
        if Item.objects.filter(subcategory=request.data['subcategory'], name=request.data['name']).exists():
            raise serializers.ValidationError('This data already exist')
        if item.is_valid():
            item.save()
            return Response(item.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request):
        if request.query_params:
            items = Item.objects.filter(**request.query_params.dict())
        else:
            items = Item.objects.all()
    
        if items:
            serializer = ItemSerializers(items, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    
    def patch(self,request, pk):

        item = Item.objects.get(pk=pk)
        data = ItemSerializers(instance=item, data=request.data, partial=True)

        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

    def delete(self,pk=None):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response({"Message":"data deleted successfully"},status=status.HTTP_202_ACCEPTED)
