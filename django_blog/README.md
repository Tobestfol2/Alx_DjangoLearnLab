## Comment System

### Features
- Authenticated users can comment on blog posts
- Users can edit or delete their own comments only
- Comments are displayed below each post with timestamp
- Comments ordered by newest first

### How to Use
1. View a blog post
2. Log in to post a comment
3. Your comments show Edit/Delete links
4. Other users' comments are read-only

### Models
- Comment has post (ForeignKey), author (User), content, created_at, updated_at
- Related name 'comments' on Post for easy access

### Permissions
- Only authenticated users can comment
- Only comment author can edit/delete