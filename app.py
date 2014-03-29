from eve import Eve

import os
import redis
import settings

# Configure redis server
if hasattr(settings, "REDIS_URI"):
    r = redis.StrictRedis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASSWORD,
        db=0
    )
else:
    r = None

app = Eve(redis=r)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)