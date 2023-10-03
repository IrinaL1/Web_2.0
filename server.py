import grpc
import user_sport_pb2_grpc as users_grpc
from user_sport_pb2 import Sports, AllSport
from sport_info import s
from concurrent import futures

#Это сервер, в нём создаём класс, который наследуется от класса, созданого в прото(service который)

class SportLiveServicer(users_grpc.SportLiveServicer):
    #Дальше идёт описание функций
    def GetSport(self, request, context):
        #Ищем человека с нужным именем, запрошеным клиентом
        for i in s:
            if i['user'] == request.name:
                user = i
                break
        return Sports(tr=user['tr'], sp=user['sp'], st=user['st'])
    

    def AllSports(self, request, context):
       #Выводим всех до количества, переданого клиентом(название переменных, которым присваиваем должно совпадать с названиями в прото файле)
        res = [Sports(user=i['user'],tr=i['tr'], sp=i['sp'], st=i['st']) for i in s]
        return AllSport(spt=res[:request.c])

#Часть которая говорит серверу какой порт слушать и каким классом пользоваться при приходе запроса 
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_grpc.add_SportLiveServicer_to_server(SportLiveServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

#Запуск сервера
if __name__ == '__main__':
    serve()