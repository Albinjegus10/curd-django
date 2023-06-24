from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from rest_framework import status
from .serializer import EmployeeSerializer
# Create your views here.


class EmployeeDetails(APIView):
    def get(self,request):
        obj=Employee.objects.all()
        serializer =EmployeeSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.data,status=status.HTTP_400_BAD_REQUEST)
