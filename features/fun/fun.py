import random
import re

from discord_http import AllowedMentions, Context, Embed
from discord_http.commands import Choice, Cog, choices, command, describe
from munch import Munch

from tools import Client
from tools.utilities.text import plural

from .api import random_image


class Fun(Cog):
    def __init__(self: "Fun", bot: Client):
        self.bot: Client = bot
        self.eightball_responses = {
            "As I see it, yes": True,
            "Better not tell you now": False,
            "Concentrate and ask again": False,
            "Don't count on it": False,
            "It is certain": True,
            "It is decidedly so": True,
            "Most likely": True,
            "My reply is no": False,
            "My sources say no": False,
            "Outlook good": True,
            "Outlook not so good": False,
            "Reply hazy, try again": False,
            "Signs point to yes": True,
            "Very doubtful": False,
            "Without a doub.": True,
            "Yes": True,
            "Yes, definitely": True,
            "You may rely on it": True,
            "Ask again later": False,
            "I can't predict now": False,
        }

    @command(name="8ball", user_install=True)
    @describe(
        question="The question you want want answers too",
    )
    async def eightball(self, ctx: Context, question: str):
        """Consult 8ball to receive an answer"""
        shakes = random.randint(1, 5)
        response = random.choice(list(self.eightball_responses.keys()))
        return ctx.response.send_message(
            embed=Embed(
                description=f"🎱 **{ctx.user.name}** shakes the 8ball {plural(shakes):shake|shakes} and asks: **{question}**\n\n🎱 **8ball says:** {response}",
                color=0x2F3136,
            )
        )

    @command(name="duck", user_install=True)
    async def duck(self, ctx: Context):
        """Posts a random duck"""
        return await random_image(ctx, "https://random-d.uk/api/v1/random", "url")

    @command(name="coffee", user_install=True)
    async def coffee(self, ctx: Context):
        """Posts a random coffee"""
        return await random_image(
            ctx, "https://coffee.alexflipnote.dev/random.json", "file"
        )

    @command(name="birb", user_install=True)
    async def birb(self, ctx: Context):
        """Posts a random birb"""
        return await random_image(ctx, "https://api.alexflipnote.dev/birb", "file")

    @command(name="sadcat", user_install=True)
    async def sadcat(self, ctx: Context):
        """Post a random sadcat"""
        return await random_image(ctx, "https://api.alexflipnote.dev/sadcat", "file")

    @command(name="cat", user_install=True)
    async def cat(self, ctx: Context):
        """Posts a random cat"""
        return await random_image(ctx, "https://api.alexflipnote.dev/cats", "file")

    @command(name="dog", user_install=True)
    async def dog(self, ctx: Context):
        """Posts a random dog"""
        return await random_image(ctx, "https://api.alexflipnote.dev/dogs", "file")

    @command(name="fox", user_install=True)
    async def fox(self, ctx: Context):
        """Posts a random fox"""
        return await random_image(ctx, "https://randomfox.ca/floof", "image")

    @command(name="coinflip", user_install=True)
    async def coinflip(self, ctx: Context):
        """Coinflip!"""

        return ctx.response.send_message(
            f"**{ctx.user.name}** flipped a coin and got **{'Heads' if random.choice([True, False]) else 'Tails'}**"
        )

    @command(name="urban", user_install=True)
    @describe(search="The search term you want to search for")
    async def urban(self, ctx: Context, search: str):
        """Search the Urban Dictionary"""
        response: Munch = await self.bot.session.request(
            "http://api.urbandictionary.com/v0/define", params=dict(term=search)
        )

        if not response.list:
            return ctx.response.send_message(
                "No results found for that search term. Try again with a different one."
            )

        def repl(match: re.Match) -> str:
            word = match[2]
            return f"[{word}](https://{word.replace(' ', '-')}.urbanup.com)"

        entry = response.list[0]

        return ctx.response.send_message(
            embed=Embed(
                url=entry.get("permalink"),
                title=entry.get("word"),
                description=re.compile(r"(\[(.+?)\])").sub(
                    repl, entry.get("definition")
                ),
            )
            .add_field(
                name="Example",
                value=re.compile(r"(\[(.+?)\])").sub(repl, entry.get("example")),
                inline=False,
            )
            .set_footer(
                text=f"👍 {entry.get('thumbs_up'):,} 👎 {entry.get('thumbs_down'):,} - {entry.get('author')}"
            )
        )

    @command(name="reverse", user_install=True)
    @describe(text="The text you want to reverse")
    async def reverse(self, ctx: Context, text: str):
        """Reverse the text you send"""
        return ctx.response.send_message(
            text[::-1], allowed_mentions=AllowedMentions.none()
        )

    @command(name="slot", user_install=True)
    async def slot(self, ctx: Context):
        """Roll the slot machine"""
        emojis = ["🍇", "🍊", "🍐", "🍒", "🍋", "🍉", "🍌", "🍓", "🍈"]
        slots = [random.choice(emojis) for _ in range(3)]

        if slots[0] == slots[1] == slots[2]:
            return ctx.response.send_message(
                f"[ {' '.join(slots)} ]\n> Congrats, you won! 🎉"
            )
        return ctx.response.send_message(
            f"[ {' '.join(slots)} ]\n> You lost, try again... 🍃"
        )

    @command(name="dice", user_install=True)
    async def dice(self, ctx: Context):
        """Dice game. Good luck"""
        bot_dice, player_dice = [random.randint(1, 6) for _ in range(2)]

        results = "\n".join(
            [
                f"**{self.bot.user.name}:** 🎲 {bot_dice}",
                f"**{ctx.user.name}** 🎲 {player_dice}",
            ]
        )

        match player_dice:
            case x if x > bot_dice:
                final_message = "Congrats, you won 🎉"
            case x if x < bot_dice:
                final_message = "You lost, try again... 🍃"
            case _:
                final_message = "It's a tie 🎲"

        return ctx.response.send_message(f"{results}\n> {final_message}")

    @command(name="roulette", user_install=True)
    @describe(color="The color you want to 'bet' on")
    @choices(
        color={
            "blue": "🔵 Blue",
            "red": "🔴 Red",
            "green": "🟢 Green",
            "yellow": "🟡 Yellow",
        }
    )
    async def roulette(self, ctx: Context, color: Choice[str]):
        """color roulette"""
        colors = {
            "🔵": "blue",
            "🔴": "red",
            "🟢": "green",
            "🟡": "yellow",
        }

        bot_color, player_color = [random.choice(list(colors.keys())) for _ in range(2)]

        results = "\n".join(
            [
                f"**{self.bot.user.name}:** {bot_color}",
                f"**{ctx.user.name}** {player_color}",
            ]
        )

        match player_color:
            case color.key if color.key == bot_color:
                final_message = "Congrats, you won 🎉"
            case _:
                final_message = "You lost, try again... 🍃"

        return ctx.response.send_message(f"{results}\n> {final_message}")
