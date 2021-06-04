import hashlib
import os

"""celery & redis"""


def celery_app():
    from celery import Celery

    return Celery(
        "worker",
        backend=_redis_url(db="CELERY_BACKEND"),
        broker=_redis_url(db="CELERY_BROKER"),
        redis_backend_use_ssl=_celery_ssl(),
        broker_use_ssl=_celery_ssl(),
    )


def redis_celery_broker():
    import redis

    return redis.Redis.from_url(_redis_url(db="CELERY_BROKER"))


def _redis_url(db):
    # different integer but alwayse the same for the same string
    db_id = int(hashlib.sha256(db.encode()).hexdigest(), 16) % 10
    local_uri = f"redis://localhost:6379/{db_id}"

    return os.getenv(f"REDIS_URI_{db}", local_uri)


def _celery_ssl():
    import ssl

    if "rediss://" in os.getenv("REDIS_URI_CELERY_BACKEND", ""):
        return {"ssl_cert_reqs": ssl.CERT_NONE}
    else:
        None


def start():
    import dotenv

    dotenv.load_dotenv()
