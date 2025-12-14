## Posts and Comments API

Base URL: `http://127.0.0.1:8000/api/`

### Posts
- **GET /posts/** → List all posts (paginated, searchable by title/content)
- **POST /posts/** → Create post (authenticated)
- **GET /posts/{id}/** → Retrieve post
- **PATCH/PUT /posts/{id}/** → Update post (owner only)
- **DELETE /posts/{id}/** → Delete post (owner only)

### Comments (Nested)
- **GET /posts/{post_id}/comments/** → List comments on post
- **POST /posts/{post_id}/comments/** → Add comment (authenticated)
- **PATCH/DELETE /posts/{post_id}/comments/{id}/** → Update/delete comment (owner only)

### Example Response (Post)
```json
{
    "id": 1,
    "author": {"id": 1, "username": "testuser"},
    "title": "My Post",
    "content": "Hello!",
    "created_at": "2025-12-15T10:00:00Z",
    "comments_count": 3,
    "comments": [...]
}