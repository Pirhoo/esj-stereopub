from eve import Eve

import os
import redis
import settings
import auth


# 
eve_conf = {}
# Configure redis server
if hasattr(settings, "REDIS_URI"):
    eve_conf["redis"] = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_PASSWORD, db=0)
# Configure basic authentication
if settings.USERNAME != None and  settings.PASSWORD != None:
    eve_conf["auth"] = auth.BasicAuth 

app = Eve(**eve_conf)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)