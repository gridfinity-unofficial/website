List models
---------------------
### Request
  `GET /api/v1/model`

### Response
  Expected Status `200 OK`

#### Response Body
  Returns a list of all currently registered models. Structure of a model in that list:

| Object Field  | Type   | Description                                      |
|---------------|--------|--------------------------------------------------|
| `id`          | string | md5 hash of (`name` + `url`)                     |
| `name`        | string | The display name of the model                    |
| `creator`     | string | The person who maid the model                    |
| `license`     | string | What the model was licensed with                 |
| `url`         | string | Direct link to model download page               |
| `images`      | list   | List of some image urls of the model             |
| `description` | string | Describes the given model                        |
| `category`    | string | What category the model might be                 |
| `grid_x`      | int    | Dimensions of the model in Gridfinity grid units |
| `grid_y`      | int    | Dimensions of the model in Gridfinity grid units |


#### Example Response:
```json
[
  {
    "id": "b0f9e00ac6e6dc78d631b71c7658e8bd",
    "name": "Gridfinity toilet paper holder",
    "creator": "Mr. Toilet",
    "license": "unimplemented",
    "url": "https://example.url/model1",
    "images": [
      "https://example.url/image1",
      "https://example.url/image2",
      "https://example.url/image3"
    ],
    "description": "It´s a toilet paper holder.",
    "grid_x": 4,
    "grid_y": 2
  }
]
```