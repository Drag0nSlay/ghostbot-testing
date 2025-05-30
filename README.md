# GhostBot - Flask Bot Docker Runner

A simple workaround to run a background Python bot alongside a Flask web app — perfect for free hosting platforms that only allow web services.

## 🌟 What This Is

Many cloud platforms offer free hosting for websites, but not for background workers or bots. This project combines:

- A background bot process (like a Discord or Telegram bot).
- A lightweight Flask app that acts as a web interface.
- A Docker-based setup that runs both together in one container.

This way, you can deploy your bot even on platforms that technically don’t support background tasks — by making the bot run silently behind a live web service.

## 💡 Why It Works

Most free platforms only keep services alive if they expose a web server. By combining a bot and a web app into one container, this setup tricks the platform into thinking it’s a standard web app — while your bot runs continuously in the background.

## 🌍 Where It Works

This project is compatible with most modern cloud platforms that support Docker and web services, including:

- Render
- Koyeb
- Railway (limited)
- Vercel
- Any VPS or container host

## 🔗 How to Use

Clone the repo, add your own bot logic, and use Docker for the deployment.
Make changes in the "cloud.sh" file according to your python files.
Main file should contain the flask/django app and bot file should contain the bot logic that has to run in background.

## 🧠 Credits

Created as a creative solution for deploying bots on free hosting services.

## Made with ♥ By FighterX

MIT License – use it freely.
