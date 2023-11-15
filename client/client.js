const publicVapidKey = "BAZIsviuWM2A77LwvLgAfx897VZpSVhby0JpN3Oo4gEa8NcJzexKwO24NaymVPAKGdBAmZMh9SfODjd4NKObJcc";

if('serviceWorker' in navigator) {
    registerServiceWorker().catch(console.log)
}

async function registerServiceWorker() {
    const register = await navigator.serviceWorker.register('./sw.js', {
        scope: '/'
    });

    const subscription = await register.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: publicVapidKey,
    });

    await fetch("/subscribe", {
        method: "POST",
        body: JSON.stringify(subscription),
        headers: {
            "Content-Type": "application/json",
        }
    })
}