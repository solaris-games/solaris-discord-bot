import hikari
import lightbulb

from src import api

bans_plugin = lightbulb.Plugin("bans")

@bans_plugin.command()
@lightbulb.command("bans", "Displays this month's Specialist bans.")
@lightbulb.implements(lightbulb.SlashCommand)
async def bans(ctx: lightbulb.Context):
    embed= (hikari.Embed())

    months_bans = api.get_bans()

    star_ban_specs = "\n".join([f"- {s['name']}" for s in months_bans["star"]])
    carrier_bans = "\n".join([f"- {s['name']}" for s in months_bans["carrier"]])
    star_bans = "\n".join([f"- {s['name']}" for s in months_bans["specialStar"]])
    
    msg = f'''### Star Spec Bans
{star_ban_specs}

### Carrier Bans
{carrier_bans}

### Star Bans
{star_bans} '''   

    embed.description = msg


    await ctx.respond(embed)


def load(bot: lightbulb.BotApp) -> None:

  bot.add_plugin(bans_plugin)

