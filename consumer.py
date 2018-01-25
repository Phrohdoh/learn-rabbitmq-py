import sys
import pika


def cb(ch, method, properties, body: bytes):
    print(f"[x] {body}")


def main():
    """Receive messages"""
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs',
                             exchange_type='direct')

    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    severities = sys.argv[1:]
    if not severities:
        sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
        sys.exit(1)

    for severity in severities:
        channel.queue_bind(exchange='logs',
                           queue=queue_name,
                           routing_key=severity)

    channel.basic_consume(cb, queue=queue_name, no_ack=True)

    print("[*] Waiting for messages. Press CTRL-C to exit.")
    channel.start_consuming()

    connection.close()

if __name__ == '__main__':
    main()
