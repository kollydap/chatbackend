from xml.etree.ElementTree import Comment
from requests import post
from rest_framework import generics,status
from account.models import User
from .models import Post,PostComment,PostPictures,Reaction,CommentComment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostCommentSerializer,PostPictureSerializer,ReactionSerializer,PostSerializer,CommentCommentSerializer

# *---------------------------------CREATE---------------------------------------------*#

@api_view(['POST',])
def create_post(request):
    user = request.user
    post = Post(author=user)
    serializer_data = PostSerializer(post, data=request.data)
    if serializer_data.is_valid():
        serializer_data.save()
        return Response(serializer_data.data,status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_404_NOT_FOUND)  

@api_view(['POST',])
def create_comment(request,pk):
    post = Post.objects.get(id=pk)
    author = request.user
    comment = PostComment(post=post, author=author)
    serializer_data= PostCommentSerializer(comment, data=request.data)
    if serializer_data.is_valid():
        serializer_data.save()
        return Response(serializer_data.data,status=status.HTTP_201_CREATED)

@api_view(['POST',])
def create_comment_comment(request,pk):
    comment = PostComment.objects.get(id=pk)
    author = request.user
    comment_comment = CommentComment(comment=comment, author=author)
    serializer_data= PostCommentSerializer(comment_comment, data=request.data)
    if serializer_data.is_valid():
        serializer_data.save()
        return Response(serializer_data.data,status=status.HTTP_201_CREATED)
    
@api_view(['POST',])
def create_reaction(request,pk):
    post = Post.objects.get(id=pk)
    author = request.user
    reaction = Reaction(post=post, author=author)
    serializer_data= PostCommentSerializer(reaction, data=request.data)
    if serializer_data.is_valid():
        serializer_data.save()
        return Response(serializer_data.data,status=status.HTTP_201_CREATED)


# *---------------------------------RETRIEVE---------------------------------------------*#
@api_view(['GET',])
def get_all_posts(request):
    post= Post.objects.all().order_by('-published_date')
    serializer_data=[PostSerializer(p).data for p in post]
    return Response(serializer_data)

@api_view(['GET',])
def get_a_post(request,pk):
    post = Post.objects.get(id=pk)
    serializer_data= PostSerializer(post)
    return Response(serializer_data.data)
    
@api_view(['GET',])
def get_post_comments(request,pk):
    '''
    This view gets all the comments for a particular post by getting the id of the post
    '''
    post = Post.objects.get(id=pk)
    comment = PostComment.objects.all().filter(post=post)
    serializer_data= [PostCommentSerializer(c).data for c in comment]
    return Response(serializer_data)

@api_view(['GET',])
def get_comment_comments(request,pk):
    '''
    This view gets all the comments for a particular comment by getting the id of the post
    '''
    comment = PostComment.objects.get(id=pk)
    comment_comment = CommentComment.objects.all().filter(comment=comment)
    serializer_data= [CommentCommentSerializer(c).data for c in comment_comment]
    return Response(serializer_data)

@api_view(['GET',])
def get_post_reactions(request,pk):
    '''
    This view gets all the reactions for a particular post by getting the id of the post
    '''
    post = Post.objects.get(id=pk)
    reactions = Reaction.objects.all().filter(post=post)
    serializer_data= [ReactionSerializer(reaction).data for reaction in reactions]
    return Response(serializer_data)
# *----------------------------UPDATE!-----------------------------------------------*#

@api_view(['PUT',])
def update_post(request,pk):
    post = Post.objects.get(id=pk)
    serializer_data = PostSerializer(post,data=request.data)
    if serializer_data.is_valid():
        serializer_data.save()
        return Response(serializer_data.data)

@api_view(['PUT',])
def update_post_comment(request,pk):
    '''
    update a comment
    '''
    comment = PostComment.objects.get(id = pk)
    serializer_data = PostCommentSerializer(comment, data=request.data)
    if serializer_data.is_valid():
        serializer_data.save()
        return Response(serializer_data.data)
    
@api_view(['PUT',])
def update_comment_comment(request,pk):
    '''
    update a comment's comment
    '''
    comment_comment = CommentComment.objects.get(id = pk)
    serializer_data = CommentCommentSerializer(comment_comment, data=request.data)
    if serializer_data.is_valid():
        serializer_data.save()
        return Response(serializer_data.data)
    
    
# *----------------------------DELETE!-----------------------------------------------*#

@api_view(['DELETE',])
def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['DELETE',])
def delete_post_comment(request,pk):
    '''
    delete a comment
    '''
    comment = PostComment.objects.get(id=pk)
    comment.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['DELETE',])
def delete_comment_comment(request,pk):
    '''
    delete a comment's comment
    '''
    comment_comment =CommentComment.objects.get(id=pk)
    comment_comment.delete()
    return Response(status=status.HTTP_200_OK)



#* var = ModelName(kwargs)  *this helps to create a new object in the database*
