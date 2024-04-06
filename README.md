# user_bot.http

> A Simple Discord User-Installable Bot Using discord.http

## Prerequisites

- Python 3.11 or higher

## Installation

1. Create a Discord Bot:

   - Visit <https://discord.com/developers/docs/intro> and create a new application.
   - Under the "Bot" tab, generate a bot token and note its application ID.
   - Under the "Installation" tab, enable "User Install" and "Guild Install"

2. Clone the Repository:

```bash
git clone https://github.com/ilyigna/user_bot.http.git
```

3. Clone the Repository:

```bash
cd user_bot.http
pip install -Ur requirements.txt
```

4. Set Up Environment Variables:

- Rename `.env.example` to `.env`.
- Fill in the following values:
  - `TOKEN`: Your bot token
  - `APPLICATION_ID`: Your application ID
  - `PUBLIC_KEY`: Your application public key

5. Run the Bot:

```bash
python3 main.py
```

6. Add the Bot a server/account:

Use the following URL, replacing YOUR_APPLICATION_ID with your application ID: <https://discord.com/oauth2/authorize?client_id=YOUR_APPLICATION_ID>

### Optional Tools

**ngrok**: Expose your local server to the internet for testing (<https://ngrok.com/>)

**ruff**: Linter for Python code (<https://github.com/astral-sh/ruff>)

**PM2**: Process manager to keep the bot running 24/7 (<https://pm2.io/>)

**Docker**: Containerization for consistent deployment (<https://www.docker.com/>)

### Additional Information

discord.http Documentation: <https://discordhttp.dev>

Setting Up Interaction URLs: <https://discord.com/developers/docs/quick-start/getting-started>
