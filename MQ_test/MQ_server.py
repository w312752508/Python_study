import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) #实例化pika连接
channel = connection.channel()  #建立隧道
 #声明queue
while True:
    channel.queue_declare(queue='hello2',durable=True)  #定义隧道队列名称“hello”
    date = input("input message:")
    channel.basic_publish(exchange='',
                          routing_key='hello2',
                          body=date,
                          properties = pika.BasicProperties(
                          delivery_mode=2, )
                          )
# connection.close()