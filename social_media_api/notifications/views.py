from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.all()
        data = [
            {
                "id": n.id,
                "actor": n.actor.username,
                "verb": n.verb,
                "target": str(n.target) if n.target else None,
                "unread": n.unread,
                "timestamp": n.timestamp
            }
            for n in notifications
        ]
        return Response(data)

    def patch(self, request):
        # Mark all as read
        request.user.notifications.filter(unread=True).update(unread=False)
        return Response({"detail": "All notifications marked as read."})