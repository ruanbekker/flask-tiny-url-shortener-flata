# flask-tiny-url-shortener-flata
URL Shortener using Python Flask backed by Flata, which is a Python JSON format document oriented database.

## Environment Variables

```
'APP_STORAGE_FILE' => defaults to: '/tmp/db.json'
'APP_BASEURL' => defaults to: localhost:5000/t'
'APP_PROTOCOL' => defaults to:  'https'
'APP_NAME' => defaults to: 'My'
```

## Running on Docker:

Using docker:

```
$ docker run -it \
  -p 80:80 \
  -e APP_STORAGE_FILE=/tmp/mydbfile.json \
  -e APP_BASEURL=tiny.mydomain.com \
  -e APP_PROTOCOL=http \
  -e APP_NAME=Flata \
  rbekker87/url-shortener:flata
```

Using docker compose:

```
$ docker-compose up --build
```

## Screenshots

Home Screen:

![](https://user-images.githubusercontent.com/567298/46149117-db377700-c269-11e8-9ff3-6aaed8e8ba19.png)

URL to shorten:

![](https://user-images.githubusercontent.com/567298/46149232-25b8f380-c26a-11e8-87ec-47c683876a53.png)

Copy Tiny URL to clipboard:

![](https://user-images.githubusercontent.com/567298/46149311-4f721a80-c26a-11e8-9b16-7d769ba6aa3f.png)

Test redirection from Tiny to Full URL:

![](https://user-images.githubusercontent.com/567298/46149494-bf80a080-c26a-11e8-8249-9aea5529732b.png)

## Resources:

- https://hub.docker.com/r/rbekker87/url-shortener/
- https://www.bestcssbuttongenerator.com
- http://doodlenerd.com/html-control/css-textbox-generator
