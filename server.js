const express = require('express');
const webpush = require('web-push');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();

//const csp = require('express-csp-header');
/*app.use(csp({
    policies: {
        'default-src': [csp.NONE],
        'img-src': [csp.SELF],
    }
}));*/

const { expressCspHeader, INLINE, NONE, SELF } = require('express-csp-header');
app.use(bodyParser.json());

app.use(express.static(path.join(__dirname, "client")))

//Борьба с блокировкой от Content Security Policy
app.use(expressCspHeader({ 
    policies: { 
        'default-src': [expressCspHeader.NONE], 
        'img-src': [expressCspHeader.SELF], 
    } 
})); 

//Ключи сгенерированы в терминале
const publicVapidKey = "BAZIsviuWM2A77LwvLgAfx897VZpSVhby0JpN3Oo4gEa8NcJzexKwO24NaymVPAKGdBAmZMh9SfODjd4NKObJcc";
const privateVapidKey = "koSsLVi4QOZboVaQM03BJ3S5dQLLI1YrCYVYXdhHo98";

webpush.setVapidDetails("mailto:email@mail.com", publicVapidKey, privateVapidKey);

app.post('/subscribe', (req, res) => {
    const subscription = req.body;
    res.status(201).json({});
    const payload = JSON.stringify({ title: "Привет", body: "This is your first push notification" });
    webpush.sendNotification(subscription, payload).catch(console.log);
})

const PORT = 5050;

app.listen(PORT, () => {
    console.log("Сервер слушает порт " + PORT);
})