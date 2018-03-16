# import pika
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# channel.queue_declare(queue="test2")
# channel.basic_publish(exchange="",
#                       routing_key="test2",
#                       body="frist test2 message")
# print("start send message...")
# connection.close()

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='test2')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='test2',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()