import json

from confluent_kafka import Consumer

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'order_tracker',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)

consumer.subscribe(["orders"])

print("Consumer is running and subscribed to 'orders' topic")

try:
    while True:
        msg = consumer.poll()
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        value = msg.value().decode("utf-8")
        order = json.loads(value)
        print(f"received order: ID : {order['order_id']} \n the Quantity : {order['quantity']} \n /"
              f"Items : {order['item']} \n from USER : {order['user']}")

except KeyboardInterrupt:
    print("Shutting down")

finally:
    consumer.close()