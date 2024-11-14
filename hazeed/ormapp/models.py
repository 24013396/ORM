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
