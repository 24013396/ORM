# Ex02 Django ORM Web Application
## Date:14-11-2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import loan,loanAdmin
admin.site.register(loan,loanAdmin)

models.py
from django.db import models    
from django.contrib import admin
class loan(models.Model):
	Name=models.CharField(max_length=10)
	income=models.IntegerField(primary_key="Refno")
	interest=models.FloatField()
	duedate=models.DateField()
	Email=models.EmailField()
class loanAdmin(admin.ModelAdmin):
	list_display=('Name','income','interest','duedate','Email')

```


## OUTPUT

![alt text](<Screenshot 2024-10-28 144654.png>)
![Screenshot 2024-11-19 122505](https://github.com/user-attachments/assets/6649bd22-2110-43c4-882d-42019a2caffd)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
