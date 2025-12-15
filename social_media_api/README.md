## User Relationships & Personalized Feed

### Follow / Unfollow Endpoints
Base URL: `http://127.0.0.1:8000/api/auth/`

- **POST /follow/<int:user_id>/**  
  Follow a user.  
  Requires authentication.  
  Example: `/follow/3/` → follow user with ID 3

- **POST /unfollow/<int:user_id>/**  
  Unfollow a user.

### Feed Endpoint
- **GET /api/feed/**  
  Returns a chronological feed of posts from:
  - Users you follow
  - Your own posts  
  Ordered by newest first.  
  Requires authentication.

### Example Feed Response
```json
[
  {
    "id": 10,
    "author": {"id": 3, "username": "alice"},
    "title": "Beautiful sunset",
    "content": "Check this out!",
    "created_at": "2025-12-15T14:30:00Z",
    "comments_count": 5,
    "comments": [...]
  }
]