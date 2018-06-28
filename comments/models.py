from django.db import models

# Create your models here.

class Comment(models.Model):
    name=models.CharField(max_length=100)
    created_time=models.DateField(auto_now_add=True)
    text = models.TextField()
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    post=models.ForeignKey('blog.Post',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text[:20]