import os
import hikari
import lightbulb
import aiohttp
import dotenv 

import miru

from src import utils

dotenv.load_dotenv()

suggestion_channel_ids = [int(id) for id in os.environ['CHAT_IDS'].split(",") if id.isdigit()]


bot = lightbulb.BotApp(
  os.environ["DISCORD_BOT_TOKEN"],
  intents=hikari.Intents.ALL,
)

miru.install(bot)  
bot.load_extensions_from("./extensions/")


@bot.listen()
async def on_starting(event: hikari.StartingEvent) -> None:
  bot.d.aio_session = aiohttp.ClientSession()
  
 
@bot.listen()
async def on_stopping(event: hikari.StoppingEvent) -> None:
  await bot.d.aio_session.close()

@bot.listen()
async def on_message(event: hikari.MessageCreateEvent):
   await auto_react(event)
   await auto_embed(event)


async def auto_embed(event: hikari.MessageCreateEvent):
   # Ensure the bot doesn't react to its own messages
    if event.author_id == bot.get_me().id:
        return
    
    await utils.try_auto_game_link(event.message)

async def auto_react(event: hikari.MessageCreateEvent):
  # Ensure the bot doesn't react to its own messages
    if event.author_id == bot.get_me().id:
        return

  # Check if the message is from a suggestion channel
    if event.channel_id in suggestion_channel_ids:
        await event.message.add_reaction("👍")
        await event.message.add_reaction("👎")


bot.run()
