import hikari
import lightbulb

from src import utils

dice_plugin = lightbulb.Plugin("dice")

@dice_plugin.command()
@lightbulb.option("dice_type", "Choose the type of dice to roll", hikari.OptionType.STRING, choices=["d2", "d4", "d6", "d8", "d10", "d12", "d20", "d100"], required=True)
@lightbulb.command("roll_dice", "Roll some dice", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def roll_dice(ctx: lightbulb.Context, dice_type: hikari.OptionType.STRING):
    embed= utils.get_base_embeded_response()

    #Map selected dice type
    dice_size = utils.map_die_type_to_int(dice_type)

    #Create the dice and then roll
    dice = utils.DiceHandler(1, dice_size)
    dice.roll_dice()
    
    dice_results = dice.final_result

    embed.description = (f'''{ctx.user.username} rolls a {dice_type}! 

**Result:** `{dice_results}` ''')
    
    await ctx.respond(embed)


def load(bot: lightbulb.BotApp) -> None:

  bot.add_plugin(dice_plugin)