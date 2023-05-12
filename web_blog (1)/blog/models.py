from django.db import models

# Create your models here.
class post(models.Model):
    blog_id= models.AutoField(primary_key=True)
    title= models.CharField(max_length=20)
    blog_post= models.TextField()
    auther_name= models.CharField(max_length=50)
    pub_date= models.CharField(max_length=10)
    slug= models.CharField(max_length=20)
    def __str__(self):
        return str(self.title) 