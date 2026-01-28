# Threads API

Create, manage, and publish content on Threads programmatically.

## Source

- **Official URL**: https://developers.facebook.com/docs/threads
- **Specification Source**: [fbsamples/threads_api](https://github.com/fbsamples/threads_api) (Postman Collection)
- **Status**: Official (converted from Postman)
- **Format**: OpenAPI 3.0

## Base URL

```
https://graph.threads.net/v1.0
```

## Authentication

Uses OAuth 2.0 with Threads-specific scopes:

```bash
# Authorization URL
https://threads.net/oauth/authorize?client_id={app-id}&redirect_uri={uri}&scope=threads_basic,threads_content_publish&response_type=code
```

## Main Endpoints

### Authorization
- `POST /oauth/access_token` - Exchange code for token
- `GET /access_token` - Get token info
- `GET /refresh_access_token` - Refresh long-lived token

### Content Publishing
- `POST /me/threads` - Create thread container
- `POST /me/threads_publish` - Publish thread
- `GET /me/threads` - Get user's threads
- `GET /{thread-id}` - Get thread details

### Profiles
- `GET /me` - Get authenticated user profile
- `GET /{user-id}` - Get user profile

### Replies
- `GET /{thread-id}/replies` - Get replies to a thread
- `GET /{thread-id}/conversation` - Get conversation thread
- `POST /me/threads` - Create reply (with `reply_to_id`)

### Insights
- `GET /me/threads_insights` - Get user insights
- `GET /{thread-id}/insights` - Get thread insights

## Quick Examples

### Create and Publish a Thread

```bash
# Step 1: Create container
curl -X POST "https://graph.threads.net/v1.0/me/threads" \
  -d "media_type=TEXT" \
  -d "text=Hello Threads!" \
  -d "access_token=TOKEN"

# Response: { "id": "container_id" }

# Step 2: Publish
curl -X POST "https://graph.threads.net/v1.0/me/threads_publish" \
  -d "creation_id={container_id}" \
  -d "access_token=TOKEN"
```

### Post with Image

```bash
curl -X POST "https://graph.threads.net/v1.0/me/threads" \
  -d "media_type=IMAGE" \
  -d "image_url=https://example.com/image.jpg" \
  -d "text=Check this out!" \
  -d "access_token=TOKEN"
```

### Reply to a Thread

```bash
curl -X POST "https://graph.threads.net/v1.0/me/threads" \
  -d "media_type=TEXT" \
  -d "text=Great post!" \
  -d "reply_to_id={thread_id}" \
  -d "access_token=TOKEN"
```

## Permissions

| Scope | Description |
|-------|-------------|
| `threads_basic` | Read profile and threads |
| `threads_content_publish` | Create and publish threads |
| `threads_manage_insights` | Access insights |
| `threads_manage_replies` | Manage replies |
| `threads_read_replies` | Read replies |

## Resources

- [Threads API Documentation](https://developers.facebook.com/docs/threads)
- [Getting Started Guide](https://developers.facebook.com/docs/threads/get-started)
- [Official Postman Collection](https://github.com/fbsamples/threads_api)
