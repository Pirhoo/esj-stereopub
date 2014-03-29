vote = {
    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    # Allow getting resources and create new ones
    'resource_methods': ['GET', 'POST', 'DELETE'],    
    'item_methods': ['GET', 'DELETE'],
    'public_methods': ['GET', 'POST'],
    'public_item_methods': ['GET'],
    # Vote schema
    'schema':  {
        'media': {
            'type': 'integer',
            'required': True
        },
        'sex': {
            'type': 'string',
            'allowed': ["male", "female"],
        },
        'age': {
            'type': 'integer'
        },
        'is_sexist': {
            'type': 'boolean',
            'required': True
        }
    }
}
