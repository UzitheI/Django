from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=50)

class Employee(models.Model):
    full_name=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=100)
    mobile_number=models.CharField(max_length=100)
    posittion=models.ForeignKey(Position,on_delete=models.CASCADE)




#primary key will be id which will be crated by the django orm itself
    

#after this i run a migration command for the app 
#python manage.py makemigrations employee_register
#this creates a python representation of all the modifications that we made

 #now to migrate it into the db we use 
    #python3 manage.py sqlmigrate employee_register 0001
#here employee register is the name of my db and 0001 are the python representation of the migrations
#to complete migration we use
    #python3 manage.py migrate
    
    