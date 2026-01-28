# WhatsApp Business Cloud API

Send messages and manage customer conversations at scale via WhatsApp.

## Source

- **Official URL**: https://developers.facebook.com/docs/whatsapp/cloud-api
- **Specification Source**: Based on official documentation
- **Status**: Documentation-based
- **Format**: OpenAPI 3.0

## Base URL

```
https://graph.facebook.com/v21.0
```

## Authentication

Uses System User Access Token with `whatsapp_business_messaging` permission:

```bash
curl -X POST "https://graph.facebook.com/v21.0/{phone-number-id}/messages" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json"
```

## Main Endpoints

### Messages
- `POST /{phone-number-id}/messages` - Send messages

### Media
- `POST /{phone-number-id}/media` - Upload media
- `GET /{media-id}` - Get media URL
- `DELETE /{media-id}` - Delete media

### Templates
- `GET /{waba-id}/message_templates` - List templates
- `POST /{waba-id}/message_templates` - Create template
- `DELETE /{waba-id}/message_templates/{name}` - Delete template

### Phone Numbers
- `GET /{phone-number-id}` - Get phone number details
- `GET /{waba-id}/phone_numbers` - List phone numbers

### Business Profile
- `GET /{phone-number-id}/whatsapp_business_profile` - Get profile
- `POST /{phone-number-id}/whatsapp_business_profile` - Update profile

## Quick Examples

### Send Text Message

```bash
curl -X POST "https://graph.facebook.com/v21.0/{phone-number-id}/messages" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "messaging_product": "whatsapp",
    "to": "1234567890",
    "type": "text",
    "text": { "body": "Hello!" }
  }'
```

### Send Template Message

```bash
curl -X POST "https://graph.facebook.com/v21.0/{phone-number-id}/messages" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "messaging_product": "whatsapp",
    "to": "1234567890",
    "type": "template",
    "template": {
      "name": "hello_world",
      "language": { "code": "en_US" }
    }
  }'
```

## Message Types

| Type | Description |
|------|-------------|
| `text` | Plain text (up to 4096 chars) |
| `image` | JPEG, PNG images |
| `video` | MP4, 3GPP videos |
| `audio` | AAC, MP3, OGG audio |
| `document` | PDF, DOC, XLS files |
| `sticker` | Static/animated stickers |
| `location` | GPS coordinates |
| `contacts` | Contact cards |
| `interactive` | Buttons, lists, CTAs |
| `template` | Pre-approved templates |
| `reaction` | Emoji reactions |

## Resources

- [WhatsApp Cloud API Documentation](https://developers.facebook.com/docs/whatsapp/cloud-api)
- [Message Templates](https://developers.facebook.com/docs/whatsapp/message-templates)
- [Webhooks Reference](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks)
