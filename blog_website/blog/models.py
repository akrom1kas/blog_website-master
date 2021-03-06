# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = HTMLField('description', null=True)
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # description = HTMLField('description', null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    photo = models.ImageField('Cover', upload_to='covers', null=True)
    Post = models.ForeignKey('Post', verbose_name="Post", on_delete=models.SET_NULL, null=True,
                                related_name='photos')

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = HTMLField('description', null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comment',
                             blank=True, null=True)
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text