# Instagram API

Manage Instagram Business and Creator accounts programmatically. Publish content, gather insights, moderate comments, and handle messaging.

## Source

- **Official URL**: https://developers.facebook.com/docs/instagram-api/
- **Specification Source**: [Meta Postman Collection](https://www.postman.com/meta/instagram)
- **Status**: Official
- **Format**: OpenAPI 3.0 (converted from Postman)

## Base URLs

| Authentication Method | Base URL |
|----------------------|----------|
| Facebook Login | `https://graph.facebook.com` |
| Instagram Login | `https://graph.instagram.com` |

## Authentication

### Facebook Login Flow
For Instagram Business accounts connected to Facebook Pages.

```bash
# Get Page Access Token
curl "https://graph.facebook.com/v21.0/me/accounts?fields=instagram_business_account,access_token&access_token=USER_TOKEN"
```

### Instagram Login Flow
For direct Instagram authentication.

```bash
# OAuth Authorization
https://api.instagram.com/oauth/authorize?client_id={app-id}&redirect_uri={uri}&scope=user_profile,user_media&response_type=code
```

## API Categories

### Facebook Login APIs
- **Token Management** - Get access tokens for Pages you manage
- **Reels Publishing** - Upload and publish Reels content

### Instagram Login APIs
- **Send API** - Send messages via Instagram Direct
- **Welcome Message Flows** - Create automated welcome flows
- **Messenger Profile** - Manage persistent menus
- **Attachment Upload** - Upload photos and media
- **Conversations** - Access conversations and messages
- **Webhooks** - Subscribe to real-time updates
- **Insights** - Access account analytics
- **Comment Moderation** - Get and reply to comments

## Quick Examples

### Publish a Reel

```bash
# Step 1: Create container
curl -X POST "https://graph.facebook.com/v21.0/{ig_user_id}/media" \
  -d "media_type=REELS" \
  -d "video_url=https://example.com/video.mp4" \
  -d "caption=My Reel" \
  -d "access_token=PAGE_TOKEN"

# Step 2: Publish
curl -X POST "https://graph.facebook.com/v21.0/{ig_user_id}/media_publish" \
  -d "creation_id={container_id}" \
  -d "access_token=PAGE_TOKEN"
```

### Get Account Insights

```bash
curl "https://graph.instagram.com/v21.0/{ig_user_id}/insights?metric=impressions,reach&period=day&access_token=TOKEN"
```

## Resources

- [Instagram Platform Documentation](https://developers.facebook.com/docs/instagram-platform)
- [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
- [Meta Postman Collections](https://www.postman.com/meta/instagram)
