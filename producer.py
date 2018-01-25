import sys
import pika


def main():
    """Send a single message to a named queue"""
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)

    message = ' '.join(sys.argv[1:]) or 'This job will take 5 seconds: .....'
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2
                          ))

    print(f"[x] Sent {message}")
    connection.close()

if __name__ == '__main__':
    main()
