import os
from flata import Flata, Query
from flata.storages import JSONStorage
from flask import Flask, request, render_template, url_for, redirect
from random import choice, randint
from string import ascii_letters

app_storage_file = os.getenv('APP_STORAGE_FILE', '/tmp/db.json')
app_tiny_baseurl = os.getenv('APP_BASEURL', 'localhost:5000/t')
app_protocol = os.getenv('APP_PROTOCOL', 'https')
app_name = os.getenv('APP_NAME', 'My')
body_text = app_name + ' URL Shortener'

db_init = Flata(app_storage_file, storage=JSONStorage)
db_init.table('collection1', id_field = 'counter_id')
db = db_init.get('collection1')
q = Query()

tiny_appurl = app_protocol + '://' + app_tiny_baseurl + '/t'

def generate_tiny():
    tiny_key = ''.join(choice(ascii_letters) + str(randint(0,9)) for x in range(randint(8, 8))).lower()
    return tiny_key

def put_url(destination_url):
    tiny_id = generate_tiny()
    tiny_url = '{}/{}'.format(tiny_appurl, tiny_id)
    db.insert({'id': tiny_id, 'name': tiny_url, 'value': destination_url})
    return tiny_url

def get_url(tiny_url):
    tiny_id = tiny_url.split('/')[-1]
    item = db.search(q.id == tiny_id)[0]
    response = item.get('value')
    return response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('index.html', body_text=body_text)

@app.route('/result', methods=['GET', 'POST'])
def result():
    url = request.form["input"]
    if 'http' in url.split('.')[0]:
        tiny_url = put_url(url)
        return render_template('result.html', body_text="Your Tiny URL", tiny_url=tiny_url)
    else:
        message = ''
        return render_template('result.html', body_text="Specify Protocol with your link", tiny_url=message)

@app.route('/t/<tinyid>')
def redirect_it(tinyid):
    full_url = get_url(tinyid)
    return redirect(full_url)

if __name__ == '__main__':
    app.run()
