import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()
channel.queue_declare(queue="test2")

def callback(ch,method,pro,body):
    print("%r"%body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,
                         queue="test2",
                         no_ack=False)
channel.start_consuming()
channel.close()
