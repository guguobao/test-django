from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    
class Blog(models.Model):
  title=models.CharField(max_length=100)
  content=models.TextField()
  
  def __unicode__(self):
    return self.content.encode('utf-8')
   
  
class Author(models.Model):
   name = models.CharField(max_length=50)
   email = models.EmailField()
 
   def __unicode__(self):  # __str__ on Python 3
       return self.name
        