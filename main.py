import asyncio
import os

import aiohttp
import discord
from dotenv import load_dotenv

import core
from core.utils import LogHandler


load_dotenv()


async def main() -> None:
    """The launch point for an instance of the bot."""

    web_client = aiohttp.ClientSession()                # Handles any web request necessities.
    logger = LogHandler()                               # Handles logging within the bot, mostly.

    async with web_client, logger:
        # Choose the extensions you want to load.
        initial_extensions = ["jishaku", "exts.help", "exts.lol"]

        async with core.Bot(
            intents=discord.Intents.all(),
            command_prefix=";",
            web_client=web_client,
            initial_extensions=initial_extensions
        ) as bot:
            await bot.start(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    asyncio.run(main())
