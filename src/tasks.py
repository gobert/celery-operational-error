import logging
import random
import time

import config


config.start()
app = config.celery_app()


@app.task
def task_one(city_name):
    logging.warning("Received: %s", city_name)

    sleep_duration = random.randint(1, 3)
    time.sleep(sleep_duration)
