from django.db import models
from django.db import connections

class studentdetails(models.Model): # Creating a class for databse migrations 
    Name=models.CharField(max_length=15)
    Position=models.CharField(max_length=25)
    Duration=models.IntegerField()
    Start_date=models.DateField()
    End_date=models.DateField()
    Stipend=models.IntegerField()
    class meta:
        db_table="studentdetails" # Database table name
