import hikari
import lightbulb

from src import api

flux_plugin = lightbulb.Plugin("fluxs")

@flux_plugin.command()
@lightbulb.command("flux", "Displays this month's Flux.")
@lightbulb.implements(lightbulb.SlashCommand)
async def flux(ctx: lightbulb.Context):
    embed= (hikari.Embed())

    months_flux = api.get_flux()
    description = months_flux["description"]
    tool_tip = months_flux["tooltip"]

    embed.description = f'''Hey **{ctx.user.username}** this months flux is:
    
{description}

* {tool_tip}

*Flux changes on the 1st of every month, for information see the wiki.*

'''

    await ctx.respond(embed)

def load(bot: lightbulb.BotApp) -> None:

  bot.add_plugin(flux_plugin)