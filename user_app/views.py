from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework import authentication
from user_app.models import User

from .serializer import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class RetreivedUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    
