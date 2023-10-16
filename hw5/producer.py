import pika
from weather_pb2 import Weather

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='weather_today')

message = Weather()
message.deg = 15
message.defin = 'Облачно'
message = message.SerializeToString()

channel.basic_publish(exchange='', routing_key='weather_today', body=message)
print("[x] Sent Weather")
connection.close()