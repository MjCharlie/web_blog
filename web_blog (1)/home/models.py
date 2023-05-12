from django.db import models

# Create your models here.
class contact(models.Model):
    c_id= models.AutoField(primary_key=True)
    email= models.CharField(max_length=100)
    desc= models.TextField()
    phone= models.CharField(max_length=13)
    name= models.CharField(max_length=50)
    def __str__(self):
        return str(self.name) 