from django.contrib import admin
from .models import User,FriendList,FriendRequest

admin.site.register(User)
admin.site.register(FriendList)
admin.site.register(FriendRequest)
# Register your models here.
