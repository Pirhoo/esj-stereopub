from os import environ

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

# Models are separated    
import models

# Deactivvate debug by default
DEBUG          = bool(environ.get('DEBUG', False))
# Deactivate HATEOAS items
HATEOAS        = False
# Drastic rate limit to avoid flooding
RATE_LIMIT_GET = (5, 60*1)
# Application models
DOMAIN         = { 'vote': models.vote }
# Disable xml support
XML            = False
# Allow CORS
X_DOMAINS      = "*"

# Redis To Go
redis_url = environ.get('REDISTOGO_URL')
if redis_url:
    url = urlparse(redis_url)
    # Register redis configuration from REDISTOGO_URL
    REDIS_HOST     = url.hostname
    REDIS_PORT     = url.port
    REDIS_PASSWORD = url.password

# Mongolab
mongolab_uri = environ.get('MONGOLAB_URI')
if mongolab_uri:
    url = urlparse(mongolab_uri)
    # Register redis configuration from MONGOLAB_URI    
    MONGO_URI      = mongolab_uri
    MONGO_PORT     = url.username
    MONGO_USERNAME = url.password
    MONGO_HOST     = url.hostname
    MONGO_PASSWORD = url.port
    MONGO_DBNAME   = url.path[1:]