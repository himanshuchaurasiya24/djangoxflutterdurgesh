from rest_framework import serializers
from .models import Company, Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = '__all__'
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # to pass compay_id in the json which is a primary key use the below command...
    company_id = serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields = '__all__'