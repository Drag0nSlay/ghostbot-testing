# GhostBot - Flask Bot Docker Runner

A simple workaround to run a background Python bot alongside a Flask web app — perfect for free hosting platforms that only allow web services.

## 🌟 What This Is

Many cloud platforms offer free hosting for websites, but not for background workers or bots. This project combines:

- A background bot process (like a Discord/Telegram/Twilio bot or background-running logic).
- A lightweight Flask app that acts as a web interface.
- A Docker-based setup that runs both together in one container.

This way, you can deploy your bot even on platforms that technically don’t support background tasks — by making the bot run silently behind a live web service.  
Since background workers are paid but web services are free, this setup gives you the best of both worlds.

You can deploy a fully working dynamic website **and** keep your bot up and running.

---

## 💡 Why It Works

Most free platforms only keep services alive if they expose a web server. By combining a bot and a web app into one container, this setup tricks the platform into thinking it’s a standard web app — while your bot runs continuously in the background.

---

## 🌍 Where It Works

This project is compatible with most modern cloud platforms that support Docker and web services, including:

- Render
- Koyeb ✅ *(Tried and Tested)*
- Railway (limited)
- Vercel *(with tricks)*
- Any VPS or container host

---

## 🔗 How to Use

Clone the repo, add your bot logic, and deploy using Docker.  
Update `Dockerfile` and `cloud.sh` as needed — especially if file names change.  
The **main** file should run the background bot, and the **app** file should contain the Flask/Django web app.

---

## 🔄 Keep It Running (UptimeRobot)

To prevent the service from going idle, set up a free [UptimeRobot](https://uptimerobot.com) monitor:

- Choose **HTTP(s)** monitor type
- Point it to `https://your-deployment-url/`
- Set interval to every 5 minutes

This will keep your web service (and background bot) alive on platforms with inactivity timeouts.

---

## ℹ️ About

GhostBot is a deployment hack that lets you run bots without paying for background workers.  
If you're building something that needs to stay online — but you’re on a free tier — this setup helps you stretch those limits.

---

## 🧠 Credits

Created as a creative solution for deploying bots on free hosting services.

---

## 👤 Made with ♥ By FighterX

Licensed under MIT — use it freely.
