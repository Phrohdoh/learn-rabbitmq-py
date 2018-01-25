import time
import pika


def cb(ch, method, properties, body: bytes):
    job_id = method.delivery_tag
    print(f"[x] Received job {job_id}: {body}")
    time.sleep(body.count(b'.'))
    print(f"[x] Done with job {job_id}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    """Receive messages"""
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(cb, queue='task_queue')

    print("[*] Waiting for messages. Press CTRL-C to exit.")
    channel.start_consuming()

    connection.close()

if __name__ == '__main__':
    main()
