## Likes & Notifications

### Likes
- **POST /api/posts/{id}/like/** → Like a post (creates notification if not own post)
- **POST /api/posts/{id}/unlike/** → Unlike a post
- Prevents duplicate likes

### Notifications
- **GET /api/notifications/** → List user's notifications (unread flagged)
- **PATCH /api/notifications/** → Mark all as read

### Notification Types
- "started following you"
- "liked your post"
- "commented on your post"

### Example Notification
```json
{
  "id": 1,
  "actor": "alice",
  "verb": "liked your post",
  "target": "My First Post",
  "unread": true,
  "timestamp": "2025-12-15T12:00:00Z"
}

## Live Deployment

**Live URL**: https://social-media-api.onrender.com

### Production Features
- Hosted on Render.com (free tier)
- PostgreSQL database
- Gunicorn web server
- WhiteNoise for static files
- Automatic HTTPS
- Environment variables for security
- Auto-deploy on Git push

### Deployment Steps
1. Connected GitHub repo to Render.com
2. Configured PostgreSQL addon
3. Set environment variables (SECRET_KEY, DATABASE_URL)
4. Used gunicorn + WhiteNoise
5. Ran collectstatic and migrate on deploy

### Maintenance
- Logs available in Render dashboard
- Auto-restart on crash
- Free tier sleeps after inactivity (wakes on request)