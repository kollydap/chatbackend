from requests import post
from rest_framework import serializers
from account.serializers import UserSerializer
from .models import Post,PostComment,PostPictures,Reaction,CommentComment


        
class PostCommentSerializer(serializers.ModelSerializer):
    # author = UserSerializer(requred=False)
    # post = PostSerializer(required=False)
    class Meta:
        model = PostComment
        fields = '__all__' 
class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__' 
        
class PostPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPictures
        fields = '__all__' 
        
class CommentCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentComment
        fields = '__all__' 
        
class PostSerializer(serializers.ModelSerializer):
    post_comment = PostCommentSerializer(read_only = True, many=True)
    post_pictures = PostPictureSerializer(read_only = True, many=True)
    post_reaction = ReactionSerializer(read_only = True, many=True)
    # comment_comment = CommentComment()
    author = UserSerializer(required = False)
    class Meta:
        model = Post
        fields = '__all__' 
        

        