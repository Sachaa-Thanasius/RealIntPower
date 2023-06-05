from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

import discord
from discord.ext import commands


if TYPE_CHECKING:
    from .bot import Bot


__all__ = ("Interaction", "Context")


# Custom interaction and context, with bot specified for the sake of easier autocomplete and dev.
# - The custom context can be expanded into a class later if necessary.
Interaction: TypeAlias = discord.Interaction["Bot"]
Context: TypeAlias = commands.Context["Bot"]
