from cStringIO import StringIO
import cPickle as pickle
from uuid import uuid4
import os, redis

if "REDIS_URL" in os.environ:
    r = redis.from_url(os.environ.get("REDIS_URL"))
else:
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

def write_to_redis(data_frame):
    data_string = StringIO()
    pickle.dump(data_frame, data_string)
    uuid = str(uuid4())
    data_string.seek(0)
    r.set(uuid, data_string.read())
    data_string.close()
    return uuid

def read_from_redis(uuid):
    data_string = StringIO(r.get(uuid))
    # r.delete(uuid)
    return pickle.load(data_string)
