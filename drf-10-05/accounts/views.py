from accounts.models import MyUser
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def user_list(request):
    users = MyUser.objects.all()
    serializer = UserSerializer(MyUser, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

