from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=50, default='Venecia')
    image= models.ImageField(upload_to='media/')
    text=models.CharField(max_length=2000)

    def save_profile(self): 
        self.save()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/')
    project_url=models.CharField(max_length=200)


    def save_project(self): 
        self.save()

    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.EmailField(default='SOME STRING')
    Github =models.CharField(max_length=100)
    LinkedIn =models.CharField(max_length=100)
    
    def save_contact(self): 
        self.save()

    def __str__(self):
        return self.email