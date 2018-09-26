# flask-tiny-url-shortener-flata
URL Shortener using Flask backed by Flata

## Environment Variables

```
'APP_STORAGE_FILE' => defaults to: '/tmp/db.json'
'APP_BASEURL' => defaults to: localhost:5000/t'
'APP_PROTOCOL' => defaults to:  'https'
'APP_NAME' => defaults to: 'My'
```

## Running on Docker:

```
$ docker run -it \
  -p 80:80 \
  -e APP_STORAGE_FILE=/tmp/mydbfile.json \
  -e APP_BASEURL=tiny.mydomain.com \
  -e APP_PROTOCOL=http \
  -e APP_NAME=Flata \
  rbekker87/url-shortener:flata
```
