# Stream Store Kafka

A real-time order tracking system built with Apache Kafka, demonstrating event-driven architecture for an e-commerce streaming store.

## 📋 Overview

This project simulates a streaming e-commerce order pipeline where:
- A **producer** publishes new order events to a Kafka topic
- A **consumer** subscribes to the topic and tracks incoming orders in real time

It serves as a practical learning project for understanding:
- Event-driven architecture and message streaming
- Apache Kafka producer/consumer patterns
- JSON-based event serialization
- Docker-based Kafka deployment with KRaft mode

## 🏗️ Architecture

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│  Order Producer  │ ──────► │   Apache Kafka   │ ──────► │  Order Tracker  │
│  (new_orders_    │  "orders"│   (KRaft Mode)   │ "orders"│  (tracker_       │
│   producer.py)   │         │  localhost:9092  │         │   consumer.py)   │
└─────────────────┘         └──────────────────┘         └─────────────────┘
```

### Components

| File | Role | Description |
|------|------|-------------|
| `new_orders_producer.py` | Producer | Creates order events and publishes them to the `orders` Kafka topic |
| `tracker_consumer.py` | Consumer | Subscribes to the `orders` topic and prints received order details |
| `docker-compose.yaml` | Infrastructure | Runs a single-node Kafka broker using Confluent Platform (KRaft mode) |

### Order Event Schema

Each order message is a JSON payload:

```json
{
  "order_id": "uuid",
  "user": "username",
  "item_id": "uuid",
  "item": "item name",
  "quantity": 2,
  "price": 3.00,
  "user_id": "uuid"
}
```

## 🚀 Getting Started

### Prerequisites

- **Python** >= 3.12
- **uv** package manager
- **Docker** and **Docker Compose**

### Clone the Repository

```bash
git clone https://github.com/mahmoudrabea01/stream_store_kafka.git
cd stream_store_kafka
```

### Setup

1. **Install dependencies** using `uv`:

```bash
uv sync
```

2. **Start Kafka** with Docker Compose:

```bash
docker-compose up -d
```

This starts a Kafka broker on `localhost:9092` using KRaft mode (no ZooKeeper required).

## ▶️ Usage

### Run the Consumer

Start the consumer first so it's ready to receive messages:

```bash
uv run python tracker_consumer.py
```

### Run the Producer

In a separate terminal, produce order events:

```bash
uv run python new_orders_producer.py
```

The consumer will display the received order details in real time.

## 🛠️ Tech Stack

- **Python** >= 3.12
- **Apache Kafka** 7.8.3 (Confluent Platform)
- **confluent-kafka** Python client
- **Docker Compose** for infrastructure
- **uv** for dependency management

## 📁 Project Structure

```
stream_store_kafka/
├── docker-compose.yaml      # Kafka broker configuration
├── new_orders_producer.py   # Kafka producer (sends orders)
├── tracker_consumer.py      # Kafka consumer (tracks orders)
├── pyproject.toml           # Project metadata and dependencies
├── uv.lock                  # Locked dependencies
├── src/                     # Package source (stub)
└── README.md                # This file
```

## 🧹 Cleanup

Stop and remove the Kafka container:

```bash
docker-compose down
```

To also remove the Kafka data volume:

```bash
docker-compose down -v
```

## 👤 Author

**Mahmoud Rabea**

- GitHub: [@mahmoudrabea01](https://github.com/mahmoudrabea01)

## 📄 License

This project is open source and available for educational purposes.
