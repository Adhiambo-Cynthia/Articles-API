from django.db import models

class Article(models.Model):
    title= models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
