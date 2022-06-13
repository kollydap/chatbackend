from django.contrib import admin
from .models import Post, PostPictures,Reaction,PostComment,CommentComment

admin.site.register(Post)
admin.site.register(PostPictures)
admin.site.register(Reaction)
admin.site.register(PostComment)
admin.site.register(CommentComment)
# Register your models here.
