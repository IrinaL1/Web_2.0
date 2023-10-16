import pika
from weather_pb2 import Weather

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='weather_today')

def callback(ch, method, properties, body):
    message = Weather()
    message.ParseFromString(body)
    print(f"[x] Received {message.deg}, {message.defin}")

channel.basic_consume('weather_today', callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()