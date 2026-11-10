import json
import uuid

from confluent_kafka import Producer

producer_config = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(producer_config)

order = {
    "order_id": str(uuid.uuid4()),
    "user": "jack",
    "item_id": str(uuid.uuid4()),
    "item": "Pizza",
    "quantity": 2,
    "price": 3.00,
    "user_id": str(uuid.uuid4())
}

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result."""
    if err:
        print('Message delivery failed. Reason: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
        print(f"delivered to [{msg.topic()}] \n partition[{msg.partition()}] \n offset {msg.offset()}\n")

value = json.dumps(order).encode("utf-8")

producer.produce(topic="orders",
                 value=value,
                 callback=delivery_report)
producer.flush()