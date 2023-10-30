import redis
import tornado.ioloop
import tornado.web
from datetime import datetime as dt
import datetime

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def today_time():
    current_time = dt.now()
    end_time = datetime.datetime(current_time.year, current_time.month, current_time.day, 23, 59, 59)
    time_delta = (end_time - current_time).total_seconds()
    return int(time_delta)


#Счетчик запросов
class Req_counter(tornado.web.RequestHandler):
    def get(self):
        global r
        if not r.exists('count'):
            r.set('count', 0)
            r.expire('count', today_time())
        r.incr('count')
        num_req = r.get('count')
        self.write(f"{r.ttl('count')}\n")
        self.write(f"Request number = {num_req}")
        if r.ttl('count') == -1:
            r.delete('count')
#Маршрутизация 
application = tornado.web.Application([
        (r"/request_counter", Req_counter)
    ])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
    