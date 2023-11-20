const http = require('http')
const ws = require('ws')

/*const server = http.createServer(function(request, response){
    console.log("Тип запроса:" + request.method);
    console.log("Заголовки");
    console.log(request.headers);

    response.end();
});
server.listen(2075);
*/
const wss = new ws.WebSocketServer({ port: 2075 });

//const wss = new ws.WebSocketServer({server});

wss.on('connection', function connection(ws) {
    console.log('Соединение установлено');
    ws.send('Ты подключился');

ws.on('message', function incoming(message) {
    console.log(`Получено сообщение: ${message}`);
  });

ws.on('error', function error(error){
    console.log(`Произошла ошибка: ${error}`);
});

  ws.on('close', function close() {
    console.log('Соединение закрыто');
  });
});