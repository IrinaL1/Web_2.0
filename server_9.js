const express = require("express");
const app = express();
const { v4: uuidv4 } = require("uuid");
const server = require('http').Server(app);

app.set('view engine', 'ejs')

const io = require("socket.io")(server);
const { ExpressPeerServer } = require("peer");
const peerServer = ExpressPeerServer(server, {
    debug: true,
});

app.use("/peerjs", peerServer);
app.use(express.static('public')); 

app.get("/", (req, res) => {
    res.redirect(`/${uuidv4()}`);
});

app.get("/:room", (req, res) => {
    //const roomId = req.params.room;
    //console.log(roomId);
    //res.render('room', {roomId});
    res.render('room', { roomId: req.params.room });
});

io.on("connection", (socket) => {
    socket.on("join-room", (roomId, userId) => {
    socket.join(roomId);
    socket.on('ready', ()=> {
    socket.to(roomId).broadcast.emit("user-connected", userId);
    });
    });
});

server.listen(3030);
