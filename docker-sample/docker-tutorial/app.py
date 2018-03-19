import time
import os
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
site_host = os.environ['HOST']
site_port = int(os.environ['PORT'])

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/count')
def count():
    count = get_hit_count()
    return 'Hello World! These are my greetings... I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host=site_host, port=site_port, debug=True)
