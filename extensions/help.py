import hikari
import lightbulb


help_plugin = lightbulb.Plugin("help")

@help_plugin.command()
@lightbulb.command("help", "Displays all commands.")
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx: lightbulb.Context):
  embed= (hikari.Embed())

  msg = f'''
Here's a list of things I can do:

\`/flux\` - Displays this month's Flux.
\`/bans\` - Displays this month's Specialist bans.
\`/leaderboard_rank\` - Displays the top 10 players by rank.
\`/leaderboard_elo\` - Displays the top 10 players by ELO rating.
\`/leaderboard_guild\` - Displays the top 10 guilds by total rank.
\`/animals\` - Dog or Cat.
\`/help\` - Displays this message again.

If you have any questions please contact a developer.` '''
  
  embed.description= msg

  await ctx.respond(embed)
  



def load(bot: lightbulb.BotApp) -> None:

  bot.add_plugin(help_plugin)