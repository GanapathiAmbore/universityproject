from django.db import models

class University(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    type_choices=(('State','State'),('Central','Central'))
    type=models.CharField(max_length=100,null=True,blank=True,choices=type_choices,default='Central')

    def __str__(self):
        return self.name

class College(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    university=models.ForeignKey(University,on_delete=models.CASCADE,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
