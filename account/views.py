from rest_framework import status
from .models import User,FriendList,FriendRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,FriendListSerializer,FriendRequestSerializer,RegistrationSerializer  

@api_view(['GET',])
def friend_list(request):
    user = request.user
    friend_list = FriendList.objects.all().filter(user=user)
    serializer_data = [FriendListSerializer(friends).data for friends in friend_list]
    return Response(serializer_data)
# todo: work on making the friendlist show names of friends instead of id from the serializer

@api_view(['GET',])
def get_user(request):
    try:
        user = request.user
        serializer_data = UserSerializer(user).data
        return Response(serializer_data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
         
@api_view(['GET',])
def get_all_user(request):
    try:
        users = User.objects.all()
        serializer_data = [UserSerializer(user).data for user in users]
        return Response(serializer_data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)  
 
 
@api_view(['GET',])
def get_user_friend_request_list(request):
    '''you can set is_active to true to see only pending request'''
    receiver = request.user
    user_friend_request_list =  FriendRequest.objects.all().filter(receiver=receiver, is_active=True)
    serializer_data = [FriendRequestSerializer(user_friend_request).data for user_friend_request in user_friend_request_list]
    return Response(serializer_data)
# todo: work on making the friendlist show names of friends instead of id from the serializer

    
@api_view(['POST',]) 
def send_friend_request(request,pk):
    sender = request.user
    receiver = User.objects.get(id = pk)
    # friend_request = FriendRequest.objects.create(sender = sender, receiver=receiver)
    friend_request = FriendRequest(sender=sender, receiver=receiver)
    serializer_data = FriendRequestSerializer(friend_request,data=request.data)
    if serializer_data.is_valid():
        serializer_data.save()
        # check serializer.data()
        return Response(serializer_data.data,status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_404_NOT_FOUND)
    

#todo: make sure every user has a friend list object created automatically after creating an account to prevent error of adding friends to friendlist
@api_view(['GET',])
def accept_friend_request(request,pk):
    friend_request = FriendRequest.objects.get(id=pk)
    friend_request.accept()
    return Response({'successful':True}, status=status.HTTP_200_OK)

@api_view(['GET',])
def reject_friend_request(request,pk):
    friend_request = FriendRequest.objects.get(id=pk)
    friend_request.decline()
    return Response({'successful':True}, status=status.HTTP_200_OK)

@api_view(['GET',])
def cancel_friend_request(request,pk):
    friend_request = FriendRequest.objects.get(id=pk)
    friend_request.cancel()
    return Response({'successful':True}, status=status.HTTP_200_OK)

@api_view(['GET',])
def unfriend(request,pk):
    user = request.user
    friend_list = FriendList.objects.get(user=user)
    removee = User.objects.get(id=pk)
    friend_list.unfriend(removee)
    return Response({'successful':True}, status=status.HTTP_200_OK)

@api_view(['POST',])
def create_user(request):
    serializer_data = RegistrationSerializer(data=request.data)
    data = {}
    if serializer_data.is_valid():
        account=serializer_data.save()
        data['response'] = "successfully registered a anew user."
        data['email']=account.email
        data['username']=account.username
        
    else:
        data = serializer_data.errors
    return Response(data)
    



        
        
        
    
     
# def accept_friend_request(request, friend_request_id):
#     friend_request = FriendRequest.objects.get(id=friend_request_id)
#     friend_request.accept()
    
#     return Response(status=status.HTTP_200_OK)