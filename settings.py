from os import environ

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

# Models are separated    
import models

# Deactivvate debug by default
DEBUG           = bool(environ.get('DEBUG', False))
# Deactivate HATEOAS items
HATEOAS         = False
# Drastic rate limit to avoid flooding
# 60 post requests in a window of 20 minutes
RATE_LIMIT_POST = (60, 60*20)
# Application models
DOMAIN          = { 'vote': models.vote }
# Disable xml support
XML             = False
# Allow CORS
X_DOMAINS       = "*"
X_HEADERS       = "X-Requested-With, content-type"
# Disable pagination
PAGINATION      = False
# Credidential
USERNAME        = environ.get('USERNAME', None)
PASSWORD        = environ.get('PASSWORD', None)

# Redis To Go
redis_url = environ.get('REDISTOGO_URL')
if redis_url:
    url = urlparse(redis_url)
    # Register redis configuration from REDISTOGO_URL
    REDIS_URI      = redis_url
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