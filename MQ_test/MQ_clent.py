import pika,time,threading,multiprocessing
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello2',durable=True)  #定义queue
def work_fun(body):
    print("Received %r" % body.decode())
    time.sleep(5)
    print(time.time())
def callback(ch, method, properties, body):
    t = threading.Thread(target=work_fun, args=(body,))
    t.start()
channel.basic_qos(prefetch_count=3)
channel.basic_consume(callback,
                      queue='hello2',
                      no_ack=True,
                      )
print('Waiting for messages..... \nTo exit press CTRL+C')
channel.start_consuming()