import redis
from app.core.config import Settings

settings = Settings()

try:
    redis_client = redis.Redis.from_url(
        settings.REDIS_URL,
        decode_responses=True,
        socket_connect_timeout=5
    )
    redis_client.ping()
    REDIS_AVAILABLE = True
except Exception as e:
    print(f"Redis connection failed: {e}")
    redis_client = None
    REDIS_AVAILABLE = False

def add_to_blacklist(token: str, expires_in: int):
    if REDIS_AVAILABLE and redis_client:
        try:
            redis_client.setex(f"blacklist:{token}", expires_in, "true")
        except Exception:
            pass

def is_blacklisted(token: str) -> bool:
    if REDIS_AVAILABLE and redis_client:
        try:
            return redis_client.exists(f"blacklist:{token}") > 0
        except Exception:
            pass
    return False
