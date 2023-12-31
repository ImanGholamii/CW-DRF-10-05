from django.contrib.auth import authenticate
from .models import MyUser
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


# Create your views here.

@api_view(['GET'])
@permission_classes([TokenAuthentication, ])
def user_list(request):
    users = MyUser.objects.all()
    serializer = UserSerializer(MyUser, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
