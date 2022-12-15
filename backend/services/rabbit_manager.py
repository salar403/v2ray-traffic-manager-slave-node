import json, pika

from backend.environments import (
    USAGE_ROUTING_KEY,
    RABBITMQ_EXCHANGE,
    RABBITMQ_HOST,
    RABBITMQ_PASSWORD,
    RABBITMQ_PORT,
    RABBITMQ_USERNAME,
    RABBITMQ_VIRTUAL_HOST,
)


class ProducerSingleton:
    __channel = None

    @staticmethod
    def get_channel():
        if ProducerSingleton.__channel is None:
            ProducerSingleton()
        else:
            if not ProducerSingleton.__channel.is_open:
                ProducerSingleton.__channel = None
                ProducerSingleton()
        return ProducerSingleton.__channel

    def __init__(self):
        if ProducerSingleton.__channel is not None:
            raise Exception("This class is a singleton class !")
        else:
            ProducerSingleton.__channel = self.get_producer_connection()

    def get_producer_connection(self):
        ProducerSingleton.__connection = pika.BlockingConnection(
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
                connection_attempts=10000
            )
        )
        return ProducerSingleton.__connection.channel()

    @staticmethod
    def close_connection():
        channel = ProducerSingleton.get_channel()
        channel.close()
        ProducerSingleton.__channel = None

def publish(body: any, routing_key: str = USAGE_ROUTING_KEY):
    channel = ProducerSingleton.get_channel()
    channel.basic_publish(
        exchange=RABBITMQ_EXCHANGE,
        routing_key=routing_key,
        body=json.dumps(body),
        properties=pika.BasicProperties(),
    )
