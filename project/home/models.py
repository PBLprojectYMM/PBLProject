from django.db import models

# Create your models here.

# class Contact(models.Model):
#     name = models.CharField(max_length= 50)
#     email = models.CharField(max_length= 50)
#     desc = models.TextField()
#     date = models.DateField(max_length=7, default='0000000', editable=False)

#     def __str__(self):
#         return self.name

class vaccine_pincode(models.Model):
    pincode = models.CharField(max_length= 7)
    date = models.DateField()