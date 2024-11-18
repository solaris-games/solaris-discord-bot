import hikari
import lightbulb
import httpx

animals_plugin = lightbulb.Plugin("animals")

@animals_plugin.command()
@lightbulb.option("animal", "Which animal to generate?", hikari.OptionType.STRING, choices=["Cat", "Dog"], required=True)
@lightbulb.command("animals", "Generate random picture of an animal", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def animals(ctx: lightbulb.Context, animal: hikari.OptionType.STRING):
  api_link = ''

  if animal == "Cat":
     api_link = 'https://api.thecatapi.com/v1/images/search'
  if animal == "Dog":
     api_link = 'https://dog.ceo/api/breeds/image/random'
  
  try:
    async with httpx.AsyncClient() as client:
      response = await client.get(api_link)
    
    response.raise_for_status()

    if animal == "Cat":
      image_url = response.json()[0]['url']
    else:
       image_url = response.json()['message']

    await ctx.respond(image_url)

  except httpx.HTTPStatusError as exc:
      await ctx.respond(f"API returned a {exc.response.status_code}")

  except Exception as e:
      await ctx.respond(f"An error occurred: {str(e)}")


def load(bot: lightbulb.BotApp) -> None:

  bot.add_plugin(animals_plugin)

