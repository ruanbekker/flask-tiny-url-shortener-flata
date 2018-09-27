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

```
$ docker run -it \
  -p 80:80 \
  -e APP_STORAGE_FILE=/tmp/mydbfile.json \
  -e APP_BASEURL=tiny.mydomain.com \
  -e APP_PROTOCOL=http \
  -e APP_NAME=Flata \
  rbekker87/url-shortener:flata
```

## Resources:

- https://hub.docker.com/r/rbekker87/url-shortener/
- https://www.bestcssbuttongenerator.com
- http://doodlenerd.com/html-control/css-textbox-generator
