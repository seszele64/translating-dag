# Official Endpoint

Simulate the **DeepL official API** to initiate translation requests. Unlimited, but frequent requests within a certain period of time will result in a 429 error.

## `/v2/translate`

### Method: **POST**

### Request Headers

| Header            | Description                           | Value                                                             |
| ----------------- | ------------------------------------- | ----------------------------------------------------------------- |
| `Content-Type`  | The content type of the request body. | `application/json`                                              |
| `Authorization` | The authorization of the request.     | `Authorization: DeepL-Auth-Key [yourAccessToken] [yourAuthKey]` |

Please note that if you want to pass two parameters at the same time, separate them with a space.

### Request Parameters

| Parameter       | Type       | Description                                 | Required  |
| --------------- | ---------- | ------------------------------------------- | --------- |
| `text`        | `string` | The text you want to translate.             | `true`  |
| `source_lang` | `string` | The language code of the source text.       | `false` |
| `target_lang` | `string` | The language code you want to translate to. | `true`  |

More details can be found in the [official API documentation](https://developers.deepl.com/docs/api-reference/translate).
