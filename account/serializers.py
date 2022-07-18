from rest_framework import serializers
from .models import User, FriendList, FriendRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','id','first_name','last_name','email','display_photo','cover_photo','dob','about','last_login','date_joined','gender'] 
        
class FriendListSerializer(serializers.ModelSerializer):
    friends = UserSerializer(read_only = True, many=True)
    class Meta:
        model = FriendList
        fields = '__all__' 
        
class FriendRequestSerializer(serializers.ModelSerializer):
    sender = UserSerializer(required=False)
    receiver = UserSerializer(required=False)
    class Meta:
        model = FriendRequest
        fields = '__all__' 

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    serializers.CharField
    class Meta:
        model = User
        fields = ['email','username','password','password2','first_name','last_name']
        extra_kwargs = {
            'password':{'write_only':True}
        }
        
    def save(self):
        user = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match'})
        user.set_password(password)
        user.save()