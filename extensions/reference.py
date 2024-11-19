import hikari
import lightbulb

from src import utils

reference_plugin = lightbulb.Plugin("reference")

@reference_plugin.command()
@lightbulb.command("lookup", "A command to look up game information to display on discord")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def lookup(ctx: lightbulb.SlashContext) -> None:
  pass

@lookup.child
@lightbulb.option("name", "Enter the name of the specalist you wish to look up", hikari.OptionType.STRING, autocomplete=True, required=True)
@lightbulb.command("carrier_specalist", "Look up information about a carrier specalist", pass_options=True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def carrier_specalist(ctx: lightbulb.SlashContext, name: hikari.OptionType.STRING)-> None:
  embed = utils.get_base_embeded_response()

  if utils.get_spec_details(name, "carrier") is None:
    await ctx.respond(f"{name} not found, please check spelling")
    return
  
  image_url, description, base_cost_credits, base_cost_specialist_credit = utils.get_spec_details(name, "carrier")

  #Build embed
  embed.title = name
  embed.set_thumbnail(image_url)
  embed.description = description
  embed.add_field("Specialist Token Cost", base_cost_specialist_credit, inline=True)
  embed.add_field("Credit Cost", base_cost_credits, inline=True)

  await ctx.respond(embed)
  

@carrier_specalist.autocomplete("name")
async def on_text_autocomplete(option: hikari.AutocompleteInteractionOption, interaction: hikari.AutocompleteInteraction):
  items = utils.get_spec_names("carrier")
  
  filtered_choices = utils.filter_choices(items, option)
  return filtered_choices

@lookup.child
@lightbulb.option("name", "Enter the name of the specalist you wish to look up", hikari.OptionType.STRING, autocomplete=True, required=True)
@lightbulb.command("star_specalist", "Look up information about a star specalist", pass_options=True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def star_specalist(ctx: lightbulb.SlashContext, name: hikari.OptionType.STRING)-> None:
  embed = utils.get_base_embeded_response()

  if utils.get_spec_details(name, "star") is None:
    await ctx.respond(f"{name} not found, please check spelling")
    return
  
  image_url, description, base_cost_credits, base_cost_specialist_credit = utils.get_spec_details(name, "star")

  #Build embed
  embed.title = name
  embed.set_thumbnail(image_url)
  embed.description = description
  embed.add_field("Specialist Token Cost", base_cost_specialist_credit, inline=True)
  embed.add_field("Credit Cost", base_cost_credits, inline=True)

  await ctx.respond(embed)
  

@star_specalist.autocomplete("name")
async def on_text_autocomplete(option: hikari.AutocompleteInteractionOption, interaction: hikari.AutocompleteInteraction):
  items = utils.get_spec_names("star")
  
  filtered_choices = utils.filter_choices(items, option)
  return filtered_choices


def load(bot: lightbulb.BotApp) -> None:

  bot.add_plugin(reference_plugin)