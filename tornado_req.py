import tornado.ioloop
import tornado.web
import os

num_req = 0

#Счетчик запросов
class Req_counter(tornado.web.RequestHandler):
    def get(self):
        global num_req
        num_req += 1
        self.write(f"Request number = {num_req}")

#Выдача файла с домашкой
class Download_hw(tornado.web.RequestHandler):
    def get(self):
        path = "./data/hw1-2.html"
        if(os.path.exists(path)):
            f = open(path, 'rb')
            data = f.read(4096)
            self.write(data)
        else:
            raise tornado.web.HTTPError(404)

#Маршрутизация 
application = tornado.web.Application([
        (r"/request_counter", Req_counter),
        (r"/data", Download_hw),
    ])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
