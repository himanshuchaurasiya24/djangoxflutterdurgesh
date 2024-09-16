from django.db import models

# Create your models here.
# Company Model
class Company(models.Model):
    company_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about= models.TextField(max_length=100)
    type = models.CharField(
        max_length=100, 
        choices=(
        ('IT', 'IT'), 
        ('Non-IT', 'Non-IT'), 
        ('Mobile Phones', 'Mobile Phones')
        )
        )
    added_date= models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name+'--'+self.location
    
# Employee Model 
class  Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    emai = models.CharField(max_length=30)
    address= models.CharField(max_length=200)
    phone =  models.IntegerField()
    about = models.CharField(max_length=100)
    position = models.CharField(max_length=30, choices=(
        ('Manager', 'Manager'),
        ('Software Developer', 'Software Developer'),
        ('Project Leader', 'Project Leader')
        )
        )
    company= models.ForeignKey(Company, on_delete=models.CASCADE)
