from rest_framework import generics

from django.contrib.auth.models import User
from .serializers import UserSerializer #QuestionSerializer, ChoiceSerializer,

class UserCreate(generics.CreateAPIView):
    """
    Create a User
    """
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()

class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

