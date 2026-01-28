# Meta Platform APIs

Official API specifications for Meta's developer platform products.

## Available APIs

| API | Description | Source | Format |
|-----|-------------|--------|--------|
| [Facebook Conversions API](./facebook-conversions/) | Server-side event tracking | [GitHub (archived)](https://github.com/facebookarchive/Facebook-Server-Side-API-Swagger) | OpenAPI 3.0 |
| [Instagram API](./instagram/) | Business & Creator account management | [Postman](https://www.postman.com/meta/instagram) | OpenAPI 3.0 |
| [WhatsApp Cloud API](./whatsapp/) | Business messaging platform | [Official Docs](https://developers.facebook.com/docs/whatsapp/cloud-api) | OpenAPI 3.0 |
| [Threads API](./threads/) | Threads content publishing | [GitHub](https://github.com/fbsamples/threads_api) | OpenAPI 3.0 |

## Base URLs

| API | Base URL |
|-----|----------|
| Facebook Graph API | `https://graph.facebook.com/v21.0` |
| Instagram Graph API (Facebook Login) | `https://graph.facebook.com/v21.0` |
| Instagram Graph API (Instagram Login) | `https://graph.instagram.com/v21.0` |
| WhatsApp Cloud API | `https://graph.facebook.com/v21.0` |
| Threads API | `https://graph.threads.net/v1.0` |

## Authentication

All Meta APIs use OAuth 2.0 with access tokens. Common token types:

- **User Access Token** - Represents a user's authorization
- **Page Access Token** - Acts on behalf of a Facebook Page
- **System User Token** - For server-to-server communication
- **App Access Token** - For app-level operations

## Resources

- [Meta for Developers](https://developers.facebook.com)
- [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
- [Access Token Debugger](https://developers.facebook.com/tools/debug/accesstoken/)
- [Meta Postman Collections](https://www.postman.com/meta)

## Contributing

Found an issue or want to add more endpoints? See the [contribution guide](../README.md#contributing).
