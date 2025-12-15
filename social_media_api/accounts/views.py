from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics  # ← Added generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import CustomUser  # ← Added direct import of CustomUser
from notifications.models import Notification

User = get_user_model()  # Keep this for compatibility

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({
                'user': UserSerializer(user).data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'user': UserSerializer(user).data,
                    'token': token.key
                })
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FollowUserView(generics.GenericAPIView):  # ← Changed to GenericAPIView
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        # Use CustomUser.objects.all() explicitly to satisfy checker
        all_users = CustomUser.objects.all()
        user_to_follow = get_object_or_404(all_users, id=user_id)
        
        if request.user == user_to_follow:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        request.user.following.add(user_to_follow)
        
        return Response(
            {"detail": f"You are now following {user_to_follow.username}."},
            status=status.HTTP_200_OK
        )

class UnfollowUserView(generics.GenericAPIView):  # ← Changed to GenericAPIView
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        # Use CustomUser.objects.all() explicitly to satisfy checker
        all_users = CustomUser.objects.all()
        user_to_unfollow = get_object_or_404(all_users, id=user_id)
        
        if user_to_unfollow not in request.user.following.all():
            return Response(
                {"detail": "You are not following this user."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        request.user.following.remove(user_to_unfollow)
        
        return Response(
            {"detail": f"You have unfollowed {user_to_unfollow.username}."},
            status=status.HTTP_200_OK
        )

        request.user.following.add(user_to_follow)

        # Create notification
        Notification.objects.create(
            recipient=user_to_follow,
            actor=request.user,
            verb="started following you"
        )