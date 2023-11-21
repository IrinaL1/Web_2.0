#скачиваем базовый образ Ubuntu в котором будем разворачивать приложение
FROM ubuntu:20.04

#Заглушка, чтобы не зависало
ARG DEBIAN_FRONTEND=noninteractive

#Скачиваем необходимые библиотеки и приложения(команды Linux)
RUN apt-get -yqq update
RUN apt-get -yqq install nodejs npm
RUN npm install
RUN npm install express ejs socket.io uuid peer@0.6.1 redis
RUN npm install -dev nodemon

#Загружаем в контейнер наши файлы и папки, сохраняя иерархию
ADD server.js /
ADD /public/script.js /public/
ADD /public/style.css /public/
ADD /views/room.ejs /views/

#Назначаем порт(соответсвует тому, что в server)
EXPOSE 3030

#Команда запуска
CMD ["nodejs", "./server.js"]