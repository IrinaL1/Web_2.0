#массив классов с данными
from user_sport_pb2 import Sports

s = [
    {
     #имя поля в прото файле:значение
     'user':'Петя',
     'tr':Sports.Trener(fio="Ф.А.Петров"),
     'sp':'Бокс',
     'st':{
         'Волейбол':Sports.Trener(fio="Б.А.Петров"),
         'Баскетбол':Sports.Trener(fio="В.А.Петров"),
        },
    },
    {
     'user':'Вася',
     'tr':Sports.Trener(fio="Ф.А.Сидоров"),
     'sp':'Шахматы',
     'st':{
         'Волейбол':Sports.Trener(fio="Б.А.Сидоров"),
         'Баскетбол':Sports.Trener(fio="В.А.Сидоров"),
        },
    },
]