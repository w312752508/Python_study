import pika,time
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello2',durable=True)  #客户端、服务器都定义queue名。因为不知道客户端、服务端哪个先启动，如果客户端不定义，且先启动了，程序会报错。
def callback(ch, method, properties, body):
    time.sleep(5)
    print("Received %r" %body.decode())
    print(time.time())
    ch.basic_ack(delivery_tag=method.delivery_tag)
channel.basic_qos(prefetch_count=1) #设置处理能力，最大允许5个消息等待处理
channel.basic_consume(callback,
                      queue='hello2',
                      # no_ack=True,   #无需客户端确认消息是否正常处理
                      no_ack=False,   #无需客户端确认消息是否正常处理
                      )
print('Waiting for messages..... \nTo exit press CTRL+C')
channel.start_consuming()