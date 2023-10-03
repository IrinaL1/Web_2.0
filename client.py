import grpc 
from user_sport_pb2 import UserName, MaxRequest
import user_sport_pb2_grpc as users_grpc
#Это клиент

#На какой порт отправляем
channel = grpc.insecure_channel('localhost:50051')
#Какой сервер на этом порту нужен
stub = users_grpc.SportLiveStub(channel)

#Функции которые выводим с этого сервера(называть также как в прото)
print(stub.AllSports(MaxRequest(c=2)))
print(stub.GetSport(UserName(name="Петя")))