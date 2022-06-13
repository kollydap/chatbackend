from django.db import models
from datetime import datetime
from account.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.TextField(max_length=900)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    publised = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.body) + str(self.author)

class PostComment(models.Model):
    author  = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    body = models.TextField(max_length=900, null=True)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True )
    comment_date = models.DateTimeField(default=datetime.now, blank=True)
    publised = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.post)
    
class CommentComment(models.Model):
    author  = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE, related_name='comment_comment')
    body = models.TextField(max_length=900, null=True)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True )
    comment_date = models.DateTimeField(default=datetime.now, blank=True)
    publised = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.comment)


    
class PostPictures(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_pictures')
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    def __str__(self):
        return str(self.post)
    
class Reaction(models.Model):
    
    REACTIONS = [
        ('HAHA','HAHA'),
        ('SAD','SAD'),
        ('ANGRY','ANGRY'),
        ('WOW','WOW'),
        ('LOVE','LOVE'),
        ('LIKE','LIKE')
    ]
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_reaction')
    author  = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    reaction  = models.CharField(choices=REACTIONS, max_length=200)
    
    
# Post.post_reaction.count()  will give all reactions in a post