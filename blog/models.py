from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Status(models.TextChoices):
        DRAFT='DT',('Draft')
        PUBLISHED='PB',('Published')

class Post(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    body=models.TextField()
    publish=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts',default=1)
    Status=models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    

    class Meta:
        ordering=['-publish']
        indexes=[
            models.Index(fields=['-publish'])
        ]
    def __str__(self):
        return f"{self.title}"

