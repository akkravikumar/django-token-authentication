from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from .serializers import PasswordSerializer
from rest_framework.decorators import list_route

def logout_user(request):
     return HttpResponse("login user")

def login_form(request):
     return HttpResponse("login Clicked ")

def get_auth_token(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            request.session['auth'] = token.key
            return HttpResponse("success "+ token.key)
    return HttpResponse("failure ")


@list_route(methods=['put'], serializer_class=PasswordSerializer)
def set_password(self, request, pk=None):
    serializer = PasswordSerializer(data=request.data)
    if serializer.is_valid():
        if not user.check_password(serializer.data.get('old_password')):
            return Response({'old_password': ['Wrong password.']}, 
                                status=status.HTTP_400_BAD_REQUEST)
        # set_password also hashes the password that the user will get
        user.set_password(serializer.data.get('new_password'))
        user.save()
        return Response({'status': 'password set'}, status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)