from functools import wraps

from flask import current_app, request

import redis_conn


def return_route_function(func):
    @wraps(func)
    def route_function():
        uuid = request.form['data_uuid']
        data_frame = redis_conn.read_from_redis(uuid)
        return func(data_frame)
    return route_function

def result_route(func):
    current_app.add_url_rule(
        '/' + func.__name__,
        view_func=return_route_function(func),
        methods=['GET', 'POST'])
