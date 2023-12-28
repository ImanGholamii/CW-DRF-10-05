from rest_framework.views import APIView
from .serializers import ItemSerializer, CategorySerializer, CustomerOrderSerializer, SellRecordSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Item, CustomerOrder, Category, SellRecord
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated


class GetItemsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @swagger_auto_schema(
        request_body=ItemSerializer,
        responses={201: 'Created', 400: 'Bad Request'}
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = ItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateItemApiView(APIView):
    @swagger_auto_schema(
        request_body=ItemSerializer,
        responses={200: 'OKAY', 400: 'BAD REQUEST'}
    )
    def put(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated:
            instance = Item.objects.get(id=pk)
            serializer = ItemSerializer(instance=instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=ItemSerializer,
        responses={200: 'OKAY', 400: 'BAD REQUEST'}
    )
    def patch(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated:
            instance = Item.objects.get(id=pk)
            serializer = ItemSerializer(instance=instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteItemApiView(APIView):
    @swagger_auto_schema(
        request_body=ItemSerializer,
        responses={204: 'No Content', 404: 'Not Found'},
    )
    def delete(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                instance = Item.objects.get(id=pk)
            except Item.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
