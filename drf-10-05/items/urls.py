from django.urls import path
from .views import GetItemsAPIView,UpdateItemApiView, DeleteItemApiView

urlpatterns = [
    path('item/', GetItemsAPIView.as_view(), name='show-items'),
    path('item/update/<int:pk>/', UpdateItemApiView.as_view(), name='update-items'),
    path('item/delete/<int:pk>/', DeleteItemApiView.as_view(), name='delete-items'),
]