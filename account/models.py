from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date, datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    GENDER = [
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    ]
    
    display_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True ,null=True)
    cover_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True ,null=True)
    gender = models.CharField(choices=GENDER ,max_length=250, blank=True ,null=True)
    about = models.TextField(max_length=200, blank=True ,null=True)
    dob = models.DateField(default=date.today, blank=True, null=True)
    
# class FollowersList(models.Model):
#     '''
#     This is the FriendList of every user
#     '''
#     user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user")
#     followers = models.ManyToManyField(User, blank=True, related_name="friends")
    
#     def __str__(self):
#         return self.user.username
    
#     #not yet friends  
#     def add_follower(self, account):
#         if not account in self.followers.all():
#             self.followers.add(account)
#             self.save()
    
#     def remove_follower(self, account):
#         if account in self.friends.all():
#             self.friends.remove(account)
#             self.save()
            
    def unfriend(self,removee):
        '''
        to remove yourself from the persons friendlist
        '''
        self.remove_friend(removee)
        friends_list = FriendList.objects.get(user=removee)
        friends_list.remove_friend(self.user)
    
class FriendList(models.Model):
    '''
    This is the FriendList of every user
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")
    
    def __str__(self):
        return self.user.username
    
    #not yet friends  
    def add_friend(self, account):
        if not account in self.friends.all():
            self.friends.add(account)
            self.save()
    
    def remove_friend(self, account):
        if account in self.friends.all():
            self.friends.remove(account)
            self.save()
            
    def unfriend(self,removee):
        '''
        to remove yourself from the persons friendlist
        '''
        self.remove_friend(removee)
        friends_list = FriendList.objects.get(user=removee)
        friends_list.remove_friend(self.user)
        
    
    def is_friend(self,friend):
        if friend in self.friends.all():
            return True
        return False
    

class FriendRequest(models.Model):
    #sender can send plenty friend request
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sender.username
    
    def accept(self):
        '''
        Accept a friend request
        Update both SENDER and RECEIVER friend lists
        '''
        #get the receiver friendlist
        receiver_friend_list = FriendList.objects.get(user=self.receiver)
        if receiver_friend_list:
            #call the addfriend method on the receiver friendlist
            receiver_friend_list.add_friend(self.sender)
            #get the receiver friendlist
            sender_friend_list=FriendList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                #The is_active is set to false meaning its no longer a friend request
                # self.delete()
                self.is_active = False
                self.save()
    
    def decline(self):
        '''
        decline a request by setting 'is_active' field to False
        '''
        self.is_active = False
        self.delete()
        # self.save()
        
    def cancel(self):
        '''
        cancel  by setting the 'is_active' field to False
        This is only different with respect to 'declining' through the notification that is generated
        '''
        self.is_active = False
        self.delete()
        # self.save()
