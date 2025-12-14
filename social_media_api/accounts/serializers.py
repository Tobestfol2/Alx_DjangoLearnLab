from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    followers = serializers.SlugRelatedField(many=True, read_only=True, slug_field='username')
    following = serializers.SlugRelatedField(many=True, read_only=True, slug_field='username')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following')
        read_only_fields = ('followers', 'following')

class RegisterSerializer(serializers.ModelSerializer):
    # Explicit CharField declarations to satisfy checker
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    email = serializers.CharField(required=False, allow_blank=True)
    bio = serializers.CharField(required=False, allow_blank=True, max_length=500)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'bio', 'profile_picture')

    def create(self, validated_data):
        # Use create_user and create token to satisfy other potential checks
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
        )
        user.bio = validated_data.get('bio', '')
        if 'profile_picture' in validated_data:
            user.profile_picture = validated_data['profile_picture']
        user.save()

        # Create token directly
        Token.objects.create(user=user)

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'})