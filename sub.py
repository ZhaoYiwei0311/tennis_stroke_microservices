import redis
import pickle

my_redis = redis.Redis(port=6379)

pubsub = my_redis.pubsub()
pubsub.subscribe('captures_1')

for message in pubsub.listen():
    if message['type'] == 'message':
        list = pickle.loads(message['data'])
        for l in list:
            print(l)
        print()