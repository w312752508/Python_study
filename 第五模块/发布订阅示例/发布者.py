import redis

conn = redis.Redis(host='127.0.0.1')
chan_pub = 'fm104.5'
msg = input(">>:")
conn.publish(chan_pub, msg)