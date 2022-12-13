import json, pika
from django.core.management.base import BaseCommand
from backend.environments import (
    RABBITMQ_HOST,
    RABBITMQ_PASSWORD,
    RABBITMQ_PORT,
    RABBITMQ_USERNAME,
    RABBITMQ_VIRTUAL_HOST,
    RABBITMQ_QUEUE,
)

from traffic.tasks import update_config


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting consumer...")
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=RABBITMQ_HOST,
                port=int(RABBITMQ_PORT),
                virtual_host=RABBITMQ_VIRTUAL_HOST,
                credentials=pika.PlainCredentials(
                    username=RABBITMQ_USERNAME,
                    password=RABBITMQ_PASSWORD,
                ),
                heartbeat=None,
                blocked_connection_timeout=300,
            )
        )
        print("creating channel...")
        channel = connection.channel()
        print("declaring queue...")
        channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
        channel.basic_consume(
            queue=RABBITMQ_QUEUE, on_message_callback=self.callback, auto_ack=True
        )
        print("Starting Consuming...")
        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        print("Received new message")
        data = json.loads(body)
        update_config.apply_async(kwargs={"config":data})
        print(data)
