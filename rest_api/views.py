from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import *
from .models import UserCustom, Role, UserRole
import json

# Create your views here.

class UserRoleView(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()

    def get(self, request):
        data = []
        for val in self.queryset:
            data.append({"username":val.user_id.username,
                    "fullname":val.user_id.fullname,
                    "role":val.role_id.role})
        return Response(data, status=status.HTTP_200_OK)
