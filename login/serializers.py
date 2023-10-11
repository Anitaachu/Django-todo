# # from django.contrib.auth.models import User
# from . models import CustomUser
# from django.contrib.auth import get_user_model
# from rest_framework import serializers, validators
# from django.contrib.auth.hashers import make_password
# from rest_framework.permissions import AllowAny

# from django.contrib import auth
# from rest_framework.exceptions import AuthenticationFailed
# from rest_framework_simplejwt.tokens import RefreshToken, TokenError

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'email','password')
#         extra_kwargs = {
#             'password' : {'write_only': True},
#             'email': {'required': True, 
#             'validators':[validators.UniqueValidator(CustomUser.objects.all(), "A user with that email already exist")]

#         }
#         }
#         def validate(self, attrs):
#             email = attrs.get('email', '')
#             username = attrs.get('username', '')
#             if not username.isalnum():
#                 raise serializers.ValidationError(
#                     self.default_error_messages)
#             return attrs

#         def create(self, validated_data):
#             password = validated_data.pop("password")
#             user = CustomUser(**validated_data)
#             user.set_password(password)
#             user.save()

#             return CustomUser.objects.create_user(**validated_data)
        

# # # class LoginSerializer(serializers.ModelSerializer):
# # #     password = serializers.CharField(max_length=120, write_only=True) 
        

# # #     class Meta:
# # #         model = CustomUser
# # #         fields = ('username', 'email','password', 'token')
# # #         extra_kwargs = {
# # #             'password' : {'write_only': True},
# # #             'token': {'read_only': True},
# # #             'email': {'required': True, 
            
 
# # #         }
# # #         }


# # class LoginSerializer(serializers.ModelSerializer):

# #     password = serializers.CharField(
# #         max_length=128, min_length=6, write_only=True)

# #     class Meta:
# #         model = User
# #         fields = ('email', 'username', 'password', 'token')

# #         read_only_fields = ['token']
 


# # # from rest_framework import serializers

# # # from login.models import CustomUser

# # # from django.contrib.auth import get_user_model
# # # User = get_user_model()



# # # class RegisterSerializer(serializers.ModelSerializer):

# # #     class Meta:
# # #         model = CustomUser
# # #         fields = ('id','first_name', 'last_name', 'username', 'email','password')



# class LoginSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=68, min_length=4,write_only=True)
#     username = serializers.CharField(max_length=255, min_length=3)
#     tokens = serializers.SerializerMethodField()
#     def get_tokens(self, obj):
#         user = CustomUser.objects.get(username=obj['username'])
#         return {
#             'refresh': user.tokens()['refresh'],
#             'access': user.tokens()['access']
#         }
#     class Meta:
#         model = CustomUser
#         fields = ['password','username','tokens']
#     def validate(self, attrs):
#         username = attrs.get('username','')
#         password = attrs.get('password','')
#         user = auth.authenticate(username=username,password=password)
#         if not user:
#             raise AuthenticationFailed('Invalid credentials, try again')
#         if not user.is_active:
#             raise AuthenticationFailed('Account disabled, contact admin')
#         return {
#             'email': user.email,
#             'username': user.username,
#             'tokens': user.tokens
#         }

from rest_framework import serializers
from .models import UserData


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "email", "username", "password"]

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       username=validated_data['username']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user