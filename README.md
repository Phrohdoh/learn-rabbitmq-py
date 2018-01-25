## Setup

```sh
$ python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt
```

## Running

1) Run `rabbitmq-server` in a separate terminal

2) Run one consumer for `error` logging:

```bash
$ python consumer.py error
```

3) Run another consumer for all severity levels:

```bash
$ python consumer.py info warning error
```

3) Then run the producer:

```bash
$ python producer.py info "Hello, world!" # change `info` to either `warning` or `error` and see what happens.
```