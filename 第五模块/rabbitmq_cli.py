import pika
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="test")

def callback(ch,met,pro,body):
    print("%r"%body)

connection.basic_consume(callback,
                         queue="test",
                         no_ack=True)
channel.start_consuming()