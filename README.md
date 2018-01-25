## Setup

```sh
$ python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt
```

## Running

1) Run `rabbitmq-server` in a separate terminal

2) Run how ever many consumers you want:

```bash
$ python consumer.py # Do this N times in N shells (or run in the background with `&`)
```

3) Then run the producer:

```bash
$ python producer.py ..... # NOTE: Each `.` represents how many seconds a job will take to run. Experiment with this value.
```

Pro-tip(tm): Run lots of producers!

```bash
$ for i in {1..10}; do python producer.py "$(seq -f '.' -s '' ${i})"; done
```

> NOTE: The above usage of `seq` only works with the BSD `seq` (which OS X / macOS ships with), gnu's `seq` will not work like this.