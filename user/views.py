from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import viewsets

#hashear pass
from django.contrib.auth.hashers import make_password

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   
   def perform_create(self, serializer):
      serializer.save(password = make_password(serializer.validated_data["password"]))