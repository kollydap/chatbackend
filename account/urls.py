
from unicodedata import name
from django.urls import path
from .views import friend_list,get_user,get_all_user, get_a_user,send_friend_request, accept_friend_request, reject_friend_request, cancel_friend_request,get_user_friend_request_list,unfriend,create_user

urlpatterns = [
    path('friend-list',friend_list,name='friend_list' ),
    path('user', get_user, name='user'),
    path('get-a-user/<int:pk>', get_a_user, name='get_a_user'),
    path('send-friend-request/<int:pk>', send_friend_request, name='send_friend_list'),
    path('accept-friend-request/<int:pk>', accept_friend_request, name='accept_friend_list'),
    path('user-friend-request-list', get_user_friend_request_list, name='user_friend_request_list'),
    path('reject-friend-request/<int:pk>', reject_friend_request, name='reject_friend_list'),
    path('unfriend/<int:pk>', unfriend, name='unfriend'),
    path('cancel-friend-request/<int:pk>', cancel_friend_request, name='cancel_friend_list'),
    path('all-user',get_all_user, name='all_user_list' ),
    path('create-user', create_user, name='create_user')
]