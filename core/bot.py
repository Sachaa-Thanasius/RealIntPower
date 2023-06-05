from __future__ import annotations

import logging

import aiohttp
import discord
from discord.ext import commands

from .context import Context


LOGGER = logging.getLogger("bot.IntCoBot")


class Bot(commands.Bot):
    """The official bot of Int Corporation."""

    def __init__(self, *args, web_client: aiohttp.ClientSession, initial_extensions: list[str], **kwargs):
        super().__init__(*args, **kwargs)
        self.web_client = web_client
        self.initial_extensions = initial_extensions

    async def setup_hook(self) -> None:

        # Load all extensions on startup.
        for extension in self.initial_extensions:
            try:
                await self.load_extension(extension)
                LOGGER.info(f"Loaded extension: {extension}")
            except commands.ExtensionError as err:
                LOGGER.error("", exc_info=err)

    async def get_context(self, origin: discord.Message | discord.Interaction, /, cls=Context) -> Context:
        return await super().get_context(origin, cls=cls)

    async def on_ready(self) -> None:
        LOGGER.info(f'Logged in as {self.user} (ID: {self.user.id})')
