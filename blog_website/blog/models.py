# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from PIL import Image

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    text = HTMLField('Text', null=True)
    # cover = models.ImageField('Cover', upload_to='covers', null=True)
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
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text