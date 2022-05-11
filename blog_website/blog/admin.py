from django.contrib import admin
from .models import Post, Comment, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Photo)

