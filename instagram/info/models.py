from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import *
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime as dt 
from tinymce.models import HTMLField


# Create your models here.

class Article(models.Model):
    image=models.ImageField(upload_to='articles/', blank=True)
    caption=HTMLField()
    pub_time=models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)



    def __str__(self):
        return self.caption

    class Meta:
        ordering=['pub_time']

    #saving function
    def save_article(self):
        self.save()

    #deleting function
    def delete_article(self):
        self.delete()



class Thread(models.Model):
    userUpVotes = models.ManyToManyField(User, blank=True, related_name='threadUpVotes')
    userDownVotes = models.ManyToManyField(User, blank=True, related_name='threadDownVotes')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_article = models.ForeignKey(Article)

    # def __str__(self):
    #     return self.name


    #saving function
    def save_thread(self):
        self.save()

    #deleting function
    def delete_thread(self):
        self.delete()


class Comment(models.Model):
    comment_text=models.TextField()
    pub_time=models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    article = models.ForeignKey(Article)

    def __str__(self):
        return self.comment_text

    class Meta:
        ordering=['pub_time']

    #saving function
    def save_comment(self):
        self.save()

    #deleting function
    def delete_comment(self):
        self.delete()

    @classmethod
    def search_by_comment_text(cls,search_term):
        user=cls.objects.filter(comment_text__icontains=search_term)

        return user

