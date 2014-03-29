vote = {
    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    # Allow getting resources and create new ones
    'resource_methods': ['GET', 'POST'],
    # Vote schema
    'schema':  {
        'media': {
            'type': 'integer'
        },
        'sex': {
            'type': 'list',
            'allowed': ["male", "female"],
        },
        'age': {
            'type': 'integer'
        },
        'is_sexist': {
            'type': 'boolean'
        }
    }
}
