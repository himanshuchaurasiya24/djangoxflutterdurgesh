from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer
# vid at 1:35:57
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class = CompanySerializer
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        print('get employees of ', pk, ' company')
        try:
            company = Company.objects.get(pk=pk)
            employees = Employee.objects.filter(company=company)
            employee_serializer = EmployeeSerializer(
            employees, 
            many= True, 
            context={'request':request})
            return Response(employee_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'Company might not be existing in the database.'})
            
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

