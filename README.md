# user_bot.http
> A simple discord user-installable bot that helps you getting started within discord.http

## Requirements
- Python 3.11 or higher
- a brain

## Useful to always have
Keep [this](https://discordhttp.dev/) saved somewhere, as this is the docs to discord.http.
All you need to know about the library is defined inside here, even code that I don't use in this example is here.

## How to set up
1. Make a bot [here](https://discord.com/developers/applications) and grab the token, application ID and public key.
2. Rename the file **.env.example** to **.env**, then fill in the required spots, such as token, application ID and public key
3. To install what you need, do **pip install -Ur requirements.txt**
4. Start the bot by having the cmd/terminal inside the bot folder and type **python main.py**
5. Make sure that your Discord bot has an Interaction URL to communicate with. You can read [here](https://discordhttp.dev/pages/getting_started.html) on how to set it up. (You can use ngrok to test it locally)
6. [**Add the bot**](https://discord.com/oauth2/authorize?client_id=YOUR_APPLICATION_ID) and you're good to go!

# Optional tools
### ngrok
If you want to test your bot locally, you can use ngrok to expose your localhost to the public. You can download it [here](https://ngrok.com/download) and follow the instructions on how to use it.

### Ruff
Ruff is a simple tool to lint your code, similar to Flake8. You can install it by doing **pip install ruff** and then run it by doing **ruff check .** in the terminal. It will lint your code and tell you if there are any issues with it.

### PM2
PM2 is a process manager that you can use to keep your bot running 24/7. You can install it by doing **npm install pm2 -g** and then run it by doing **pm2 start main.py**. You can also use the ecosystem file to configure your bot to restart if it crashes.

### Docker
Docker is a nice alternative to PM2, as it can run your bot in a container. You can install it by following the instructions [here](https://docs.docker.com/get-docker/) and then run it by doing **docker compose up -d**. You can also use the Dockerfile to build your own image.