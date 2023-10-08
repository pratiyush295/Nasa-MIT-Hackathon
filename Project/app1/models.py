from django.db import models

# Create your models here.



class Authenticator(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=200 )



class Contact(models.Model):
    name=models.CharField(max_length=200)
    number=models.IntegerField(max_length=10)
    location=models.CharField(max_length=1000)


# class ImageWithCharField(models.Model):
#     latitude=models.CharField(max_length=50)
#     longitude=models.CharField(max_length=50)
#     context=models.CharField(max_length=100)
#     image = models.ImageField(null=True,upload_to='images/')

#     def __str__(self):
#         return self.title
    

class Concern(models.Model):
      latitude=models.CharField(max_length=50)
      longitude=models.CharField(max_length=50)
      context=models.CharField(max_length=100)
      image = models.ImageField(null=True,upload_to='image/')
      def __str__(self):
        return self.context


# class ConernImage(models.Model):
#     image = models.ImageField(upload_to='concernImages/')
#     title = models.CharField(max_length=100)
#     def __str__(self):
#         return self.title

