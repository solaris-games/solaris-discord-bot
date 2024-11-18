import hikari
import lightbulb

from texttable import Texttable
from src import api


leaderboard_plugin = lightbulb.Plugin("leaderboard")

@leaderboard_plugin.command()
@lightbulb.command("leaderboard_elo", "Display the top 10 players by ELO.")
@lightbulb.implements(lightbulb.SlashCommand)
async def leaderboard_elo(ctx: lightbulb.Context):
   embed= (hikari.Embed())
   leaderboard_info = api.get_elo_leaderboard()

   # Create a table using texttable
   table = Texttable()
   table.set_cols_align(["l", "l", "r"])  
   table.header(["#", "Name", "ELO"])

   # Add each player to the table
   for user in leaderboard_info["leaderboard"]:
        table.add_row([user["position"], user["username"], user["achievements"]["eloRating"]])
   
   response = f"```\n{table.draw()}\n```"
   embed.title = "Top 10 Solaris Players- ELO"
   
   embed.description = response
   
   await ctx.respond(embed)

@leaderboard_plugin.command()
@lightbulb.command("leaderboard_rank", "Display the top 10 players by rank")
@lightbulb.implements(lightbulb.SlashCommand)
async def leaderboard_rank(ctx: lightbulb.Context):
    embed= (hikari.Embed())
    leaderboard_info =  api.get_global_leaderboard()

    # Create a table using texttable
    table = Texttable()
    table.set_cols_align(["l", "l", "r"])  
    table.header(["#", "Name", "Rank"])
    
    # Add each player to the table
    for user in leaderboard_info["leaderboard"]:
        table.add_row([user["position"], user["username"], user["achievements"]["rank"]])

  
    response = f"```\n{table.draw()}\n```"

    embed.title = "Top 10 Solaris Players- Rank"
    embed.description = response

 
    await ctx.respond(embed)

@leaderboard_plugin.command()
@lightbulb.command("leaderboard_guild", "Display the top 10 guilds.")
@lightbulb.implements(lightbulb.SlashCommand)
async def leaderboard_guild(ctx: lightbulb.Context):
    embed= (hikari.Embed())
    leaderboard_info =  api.get_guild_leaderboard()

    # Create a table using texttable
    table = Texttable()
    table.set_cols_align(["l", "l", "c", "r"])  
    table.header(["#", "Name", "Tag", "Rank"])
    
    # Add each player to the table
    for guild in leaderboard_info["leaderboard"]:
        table.add_row([guild["position"], guild["name"], guild["tag"], guild["totalRank"]])

  
    response = f"```\n{table.draw()}\n```"

    embed.title = "Top 10 Solaris Guilds"
    embed.description = response

 
    await ctx.respond(embed)


def load(bot: lightbulb.BotApp) -> None:

  bot.add_plugin(leaderboard_plugin)