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

[**ngrok**](https://ngrok.com) (Expose your local server to the internet for testing)

[**ruff**](https://github.com/astral-sh/ruff) (An extremely fast Python linter and code formatter, written in Rust)

[**PM2**](https://pm2.io) (Node.js Production Process Manager with a built-in Load Balancer)

[**Docker**](https://www.docker.com) (A collaborative project for the container ecosystem to assemble container-based systems)

### Additional Information

discord.http Documentation: <https://discordhttp.alexflipnote.dev>
Setting Up Interaction URLs: <https://discord.com/developers/docs/quick-start/getting-started>
