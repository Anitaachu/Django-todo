# from django.shortcuts import render
# from rest_framework import response, status, permissions
# from rest_framework import generics
# from rest_framework.generics import GenericAPIView
# from django.contrib.auth.models import User
# from rest_framework.response import Response
# from .serializers import RegisterSerializer, LoginSerializer
# from django.contrib.auth import authenticate
# from rest_framework.permissions import AllowAny

# from django.contrib.auth import get_user_model
# User = get_user_model()



# # Create your views here.

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
#     Permission_classes = (AllowAny,)

#     def post (self, request):
#         serializer = RegisterSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)



# # class LoginView(GenericAPIView):

# #     authentication_classes = []

# #     serializer_class = LoginSerializer

# #     def post(self, request, **kwargs):
# #         email = request.data.get('email', None)
# #         password = request.data.get('password', None)

# #         user=authenticate(email=email, password=password)


# #         if user: 
# #             serializer=self.serializer_class(user)

# #             return response.Response(serializer.data, status=status.HTTP_200_OK)
        
# #         return response.Response({'message': "Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)

# class LoginAPIView(GenericAPIView):
#     serializer_class = LoginSerializer


#     def post(self,request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)


from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from . models import UserData
from rest_framework.response import Response
from rest_framework import response, status, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny


# view for registering users
class RegisterView(generics.CreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer
    Permission_classes = (AllowAny,)
    

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    


class AuthUserAPIView(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request):
        User = request.user
        serializer = UserSerializer(User)
        return response.Response({'user': serializer.data})