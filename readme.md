# Wallhaven API for Python #
## Description
Not implemented
## Quick Documentation
Import WallhavenApi package:
```python
import WallhavenApi
```
Initialize WallhavenApi:
```python
wallhaven_api= WallhavenApi.WallhavenApi()
```
If you have an account on **[Wallhaven](https://wallhaven.cc)**, you can use it to login and access all available wallpapers:
```python
wallhaven_api = WallhavenApi.WallhavenApi(username="username", password="password")
```
You can also use secure connection to **[Wallhaven](https://wallhaven.cc)**:
```python
wallhaven_api = WallhavenApi.WallhavenApi(verify_connection=True)
```
## Methods
### `wallhaven_api.get_pages_count(category_general, category_anime, category_people, purity_sfw, purity_sketchy, purity_nsfw, resolutions, ratios, sorting, order, page)`
*Returns* {Int, None}: count of pages
### `wallhaven_api.get_images_urls(category_general, category_anime, category_people, purity_sfw, purity_sketchy, purity_nsfw, resolutions, ratios, sorting, order, page)`
*Returns* {[Strings]}: array of images urls
### `wallhaven_api.get_images_numbers(category_general, category_anime, category_people, purity_sfw, purity_sketchy, purity_nsfw, resolutions, ratios, sorting, order, page)`
*Returns* {[Strings]}: array of images numbers
### `wallhaven_api.is_image_exists(image_number)`
*Returns* {Boolean}: detects if image exists
### `wallhaven_api.get_image_data(image_number)`
*Returns* {Json}: parameters of image

Example:
```json
{
    "Uploader": {
        "Username": "Cryzeen",
        "Avatar": {
            "32": "static.wallhaven.cc/images/user/avatar/32/88745_adbc0e09e7ff813ba295ad45516d41f8aac3c300d932d0f8ca009f6d8bc61a6e.jpg",
            "200": "static.wallhaven.cc/images/user/avatar/200/88745_adbc0e09e7ff813ba295ad45516d41f8aac3c300d932d0f8ca009f6d8bc61a6e.jpg"
        }
    },
    "Category": "People",
    "ShortUrl": "https://whvn.cc/341690",
    "UploadTime": "2016-03-01T10:42:09+00:00",
    "Tags": ["women", "Asian", "brown eyes", "lingerie", "cleavage", "black bras", "black panties", "high heels", "red lipstick"],
    "Ratio": "Non-standard",
    "Resolution": "2048x1367",
    "ImageColors": ["#cccccc", "#424153", "#999999", "#996633", "#ffffff"],
    "Favorites": 20,
    "ImageUrl": "https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-341690.jpg",
    "Size": "480.8 KiB",
    "Purity": "Sketchy",
    "Views": 767
}
```
## Parameters
`category_general {Boolean}` - search in General category

`category_anime {Boolean}` - search in Anime category

`category_people {Boolean}` - search in People category

`purity_sfw {Boolean}` - images with sfw purity

`purity_sketchy {Boolean}` - images with sketchy purity

`purity_nsfw {Boolean}` - images with nsfw purity

`resolutions {String}` - string of resolutions (specify a comma, can be empty)

`ratios {String}` - string of ratios (specify a comma, can be empty)

`sorting {String}` - one of this: relevance, random, date_added, views, favorites

`order {String}` - one of this: desc, asc

`page {Int}` - page of images

`image_number {String}` - image number