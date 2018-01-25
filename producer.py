import sys
import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs',
                             exchange_type='direct')

    severity = sys.argv[1] if len(sys.argv) > 2 else 'info'
    message = ' '.join(sys.argv[2:]) or 'Hello World!'

    channel.basic_publish(exchange='logs',
                          routing_key=severity,
                          body=message)

    print(f"[x] Sent {severity}: {message}")
    connection.close()

if __name__ == '__main__':
    main()
