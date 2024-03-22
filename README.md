# user_bot.http
### a fork of [discord_bot.http](https://github.com/AlexFlipnote/discord_bot.http)
🍺 A simple discord installable bot that helps you getting started within discord.http

Do you need more help? Visit my server here: **https://discord.gg/AlexFlipnote** 🍺

## Requirements
- Python 3.11 - https://www.python.org/downloads/
- Discord bot

## Useful to always have
Keep [this](https://discordhttp.dev/) saved somewhere, as this is the docs to discord.http.
All you need to know about the library is defined inside here, even code that I don't use in this example is here.

This code is also made to be as typing friendly as possible with comments and everything.
I recommend having Visual Studio Code with the Python extension installed to help you out with the code.

## How to setup
1. Make a bot [here](https://discordapp.com/developers/applications/me) and grab the token, application ID and public key.
2. Rename the file **.env.example** to **.env**, then fill in the required spots, such as token, prefix and public key
3. To install what you need, do **pip install -r requirements.txt**
4. Start the bot by having the cmd/terminal inside the bot folder and type **python index.py**
5. Make sure that your Discord bot has an Interaction URL to communicate with. You can read [here](https://discordhttp.dev/pages/getting_started.html) on how to set it up. The TLDR is that you need to expose your IP/domain to the public in order for Discord to communicate with your bot.
6. You're done, enjoy your bot!

## FAQ
Q: I don't see my bot on my server!<br>
A: Invite it by using this URL: https://discord.com/oauth2/authorize?client_id=APPLICATION_ID<br>
Remember to replace **APPLICATION_ID** with your bot Application ID

Q: There aren't that many commands here...<br>
A: Yes, I will only provide a few commands to get you started, maybe adding more later.

Q: This looks very similar to your other project discord_bot.py, why?<br>
A: Because I wanted an example as well for the discord.http library that uses interactions only.

# Optional tools
### ngrok
ngrok is a tool that allows you to expose your local IP/domain to the public, which is required for Discord to communicate with your bot. You can download it [here](https://ngrok.com/download). Once you have it downloaded, open up a cmd/terminal inside the folder and type `ngrok http 8080`. This will expose your local IP to the public, which you can use to set up your bot. It's only recommended to use this if you're testing your bot locally, otherwise you should use a domain instead with the usage of a reverse proxy using either nginx, apache2 or similar.

### Flake8
Flake8 is a tool that helps you keep your code clean. Most coding softwares will have a plugin that supports this Python module so it can be integrated with your IDE. To install it, simply do `pip install flake8`. If you're using python 3.7, install by doing `pip install -e git+https://gitlab.com/pycqa/flake8#egg=flake8`

### PM2
PM2 is an alternative script provided by NodeJS, which will reboot your bot whenever it crashes and keep it up with a nice status. You can install it by doing `npm install -g pm2` and you should be done. Keep in mind that this PM2 file is made to work on my own Linux instance, you might need to change the `interpreter` value.
```
# Start the bot
pm2 start pm2.json

# Tips on common commands
pm2 <command> [name]
  start user_bot.http   Run the bot again if it's offline
  list                     Get a full list of all available services
  stop user_bot.http    Stop the bot
  reboot user_bot.http  Reboot the bot
```
