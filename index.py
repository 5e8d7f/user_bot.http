from utils.data import CustomClient
from dotenv import dotenv_values

config = dotenv_values(".env")

client = CustomClient(
    token=config["DISCORD_TOKEN"],
    application_id=config["DISCORD_APPLICATION_ID"],
    public_key=config["DISCORD_PUBLIC_KEY"],
    sync=config["DISCORD_SYNC"].lower() == "true",
    config=config
)

client.start(
    host=config["HTTP_HOST"],
    port=config["HTTP_PORT"]
)
