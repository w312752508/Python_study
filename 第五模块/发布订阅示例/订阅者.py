import redis

conn = redis.Redis(host='127.0.0.1')
chan_sub = 'fm104.5'

pub = conn.pubsub()
pub.subscribe(chan_sub)
pub.parse_response()

while True:
    msg = pub.parse_response()
    print(msg[-1])