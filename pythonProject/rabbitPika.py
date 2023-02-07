import pika


def send(id):
    AMQP_URL = "amqps://klbnebnu:suSO0YERE2sviZgWoLvK-g5OH83wXyNI@chimpanzee.rmq.cloudamqp.com/klbnebnu"

    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='hw1')

    channel.basic_publish(exchange='', routing_key='hw1', body=id)
    print(" [x] Sent " + id)
    connection.close()
