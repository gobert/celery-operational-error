# celery-operational-error

Code to reproduce [OperationalError("\nCannot route message for exchange 'reply.celery.pidbox': Table empty or key no longer exists.\nProbably the key ('_kombu.binding.reply.celery.pidbox') has been removed from the Redis database.\n",)](https://github.com/celery/kombu/issues/1063)

### 0. Set up
* Required: `docker` (tested with v20.10.5)
* Start redis `docker run -p 6379:6379 redis:6.2.4`
* Build docker image `./bin/dev/docker-build.sh`
* Start a docker container `./bin/dev/docker-start.sh`


### 1. All seems OK
* Start 1 worker
```
./bin/dev/docker-exec.sh poetry run bin/fit_worker.sh
```
* Enqueue the tasks: `./bin/dev/docker-exec.sh poetry run python bin/fit.py`
* Check the logs: all is good

### 2. Reproduce the bug
* Start 1 worker
```
./bin/dev/docker-exec.sh poetry run bin/fit_worker.sh
```
* Enqueue the tasks: `./bin/dev/docker-exec.sh poetry run python bin/fit.py`
* Start another worker
```
./bin/dev/docker-exec.sh poetry run bin/fit_worker.sh
```
* Check the logs (of the first worker):
```
[2021-06-04 11:45:28,104: ERROR/MainProcess] Control command error: OperationalError("\nCannot route message for exchange 'reply.celery.pidbox': Table empty or key no longer exists.\nProbably the key ('_kombu.binding.reply.celery.pidbox') has been removed from the Redis database.\n")
Traceback (most recent call last):
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/connection.py", line 448, in _reraise_as_library_errors
    yield
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/connection.py", line 525, in _ensured
    return fun(*args, **kwargs)
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/messaging.py", line 199, in _publish
    return channel.basic_publish(
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/transport/virtual/base.py", line 601, in basic_publish
    return self.typeof(exchange).deliver(
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/transport/virtual/exchange.py", line 69, in deliver
    for queue in _lookup(exchange, routing_key):
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/transport/virtual/base.py", line 711, in _lookup
    self.get_table(exchange),
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/transport/redis.py", line 884, in get_table
    raise InconsistencyError(NO_ROUTE_ERROR.format(exchange, key))
kombu.exceptions.InconsistencyError:
Cannot route message for exchange 'reply.celery.pidbox': Table empty or key no longer exists.
Probably the key ('_kombu.binding.reply.celery.pidbox') has been removed from the Redis database.


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/celery/worker/pidbox.py", line 44, in on_message
    self.node.handle_message(body, message)
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/pidbox.py", line 143, in handle_message
    return self.dispatch(**body)
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/pidbox.py", line 110, in dispatch
    self.reply({self.hostname: reply},
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/pidbox.py", line 147, in reply
    self.mailbox._publish_reply(data, exchange, routing_key, ticket,
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/pidbox.py", line 278, in _publish_reply
    producer.publish(
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/messaging.py", line 177, in publish
    return _publish(
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/connection.py", line 558, in _ensured
    errback and errback(exc, 0)
  File "/usr/local/lib/python3.9/contextlib.py", line 135, in __exit__
    self.gen.throw(type, value, traceback)
  File "/home/jumbo/.cache/pypoetry/virtualenvs/celery-operational-error-EnymNbCe-py3.9/lib/python3.9/site-packages/kombu/connection.py", line 452, in _reraise_as_library_errors
    raise ConnectionError(str(exc)) from exc
kombu.exceptions.OperationalError:
Cannot route message for exchange 'reply.celery.pidbox': Table empty or key no longer exists.
Probably the key ('_kombu.binding.reply.celery.pidbox') has been removed from the Redis database.

```
