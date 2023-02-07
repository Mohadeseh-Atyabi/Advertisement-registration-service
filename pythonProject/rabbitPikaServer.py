import os
import pika
import sys
from abrArvan import AbrArvan
import imagga
from mongoDB import MongoDB
import mailgun


def receiver():
    AMQP_URL = "amqps://klbnebnu:suSO0YERE2sviZgWoLvK-g5OH83wXyNI@chimpanzee.rmq.cloudamqp.com/klbnebnu"
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='hw1')

    channel.basic_consume(queue='hw1', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    id = int(body)

    abrarvan = AbrArvan()
    abrarvan.download(str(id))
    print("Image is downloaded.")

    description, tag = imagga.tag("C:/Users/ASUS/OneDrive/Desktop/Folders/computer engineering/Principles of Cloud Computing/HW1/pythonProject/static/IMG/" + str(id) + ".jpg")
    print("Image is tagged.")

    mongo = MongoDB()
    email = mongo.show(str(id))['email']

    if description == "accepted":
        mongo.update(str(id), "Accepted", tag)
        mailgun.send_simple_message(email, "Accepted", "Your advertisement with ID " + str(id) + " is accepted :)")
    else:
        mongo.update(str(id), "Rejected", None)
        mailgun.send_simple_message(email, "Rejected", "Your advertisement with ID " + str(id) + " is rejected :(")

    print("Data is updated and email is sent.")


if __name__ == '__main__':
    try:
        receiver()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
