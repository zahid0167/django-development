from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')

    blog_title = models.CharField(max_length=265, verbose_name="Put a title")

    slug = models.SlugField(max_length=265, unique=True)

    blog_content = models.TextField(verbose_name="What is your mind")

    blog_image = models.ImageField(upload_to='blog_image')

    publish_date= models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):

        return self.blog_title



class Comment(models.Model):

    blog =models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')

    comment = models.TextField()

    coment_date = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ('-coment_date',)


    def __str__(self):

        return self.coment

    
    
