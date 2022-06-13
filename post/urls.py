from django.urls import path
from .views import create_post,get_a_post,delete_post,get_all_posts,get_post_comments,update_post_comment,delete_post_comment,delete_comment_comment,create_comment,create_reaction,create_comment_comment,get_comment_comments,get_post_reactions,update_comment_comment,update_post
urlpatterns = [
    path('create-post',create_post,name='create_post' ),
    path('<int:pk>',get_a_post,name='get_post'),
    path('',get_all_posts,name='get_all_posts'),
    path('delete-post/<int:pk>',delete_post,name='delete_post'),
    path('get-post-comments/<int:pk>',get_post_comments,name='get_post_comments'),
    path('get-comment-comments/<int:pk>',get_comment_comments,name='get_comment_comments'),
    path('get-post-reactions/<int:pk>',get_post_reactions,name='get_post_reactions'),
    path('get-post-comments/<int:pk>',get_post_comments,name='get_post_comments'),
    path('update-comment-comment/<int:pk>',update_comment_comment,name='update_comment_comment'),
    path('update-post-comment/<int:pk>',update_post_comment,name='update_post_comment'),
    path('update-post/<int:pk>',update_post,name='update_post'),
    path('delete-post-comment/<int:pk>',delete_post_comment,name='delete_post_comment'),
    path('delete-comment-comment/<int:pk>',delete_comment_comment,name='delete_comment_comment'),
    path('create-comment/<int:pk>',create_comment,name='create_comment'),
    path('delete-post-comment/<int:pk>',delete_post_comment,name='delete_post_comment'),
    path('create-comment-comment/<int:pk>',create_comment_comment,name='create_comment_comment'),
    path('create-reaction/<int:pk>',create_reaction,name='create_reaction'),

]