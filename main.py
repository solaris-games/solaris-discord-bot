import os
import hikari
import lightbulb
import aiohttp
import dotenv 

import miru

from src import utils

if 'ENV_FILE_PATH' in os.environ:
    env_file_path = os.environ['ENV_FILE_PATH']

    if env_file_path and os.path.exists(env_file_path):
        dotenv.load_dotenv(env_file_path)
    else:
        print("Failed to load additional env file from path: ", env_file_path)

dotenv.load_dotenv()

suggestion_channel_ids = [int(id) for id in os.environ['CHAT_IDS'].split(",") if id.isdigit()]

honeypot_channel_ids = [int(id) for id in os.environ['HONEYPOT_IDS'].split(",") if id.isdigit()]

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
    handled1 = await check_honeypot(event)
    if handled1:
        return
    await auto_react(event)
    await auto_embed(event)


async def check_honeypot(event: hikari.MessageCreateEvent):
    if event.channel_id in honeypot_channel_ids:
        app = event.app
        author = event.author

        try:
            channel = event.get_channel()
            if not event.guild_id:
                return True

            if event.is_bot:
                return True

            guild = await app.rest.fetch_guild(event.guild_id)
            channel = await app.rest.fetch_channel(event.channel_id)
            bot_member = guild.get_member(event.app.application.id)

            roles = await bot_member.fetch_roles()
            permissions = hikari.Permissions.NONE
            for role in roles:
                permissions |= role.permissions

            can_ban = (permissions & hikari.Permissions.BAN_MEMBERS) == hikari.Permissions.BAN_MEMBERS

            if not can_ban:
                print("Bot is missing permissions")
                return True

            await app.rest.ban_user(
                guild=event.guild_id,
                user=author.id,
                reason="Rule violation",
                delete_message_seconds=3600
            )
            print(f"Banned {author}")
            return True

        except hikari.ForbiddenError:
            print("Missing permissions or role hierarchy issue")

        except hikari.NotFoundError:
            print("User already banned or not found")

        return True
    else:
        return False

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
