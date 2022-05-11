from django.contrib import admin
from .models import Post, Comment, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

# class PostReviewAdmin(admin.ModelAdmin):
#     list_display = ('text', 'title', 'created_date', 'published_date', 'reviewer')
#
# admin.site.register(PostReview, PostReviewAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Photo)

