from os import environ

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

# Models are separated    
import models

# Deactivvate debug by default
DEBUG   = bool(environ.get('DEBUG', False))
# Deactivate HATEOAS items
HATEOAS = False
# Application models
DOMAIN  = {
    'vote': models.vote,
}

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
    MONGO_URI        = mongolab_uri
    MONGODB_USER     = url.username
    MONGODB_PASSWORD = url.password
    MONGODB_HOST     = url.hostname
    MONGODB_PORT     = url.port
    MONGODB_DB       = url.path[1:]