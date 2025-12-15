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