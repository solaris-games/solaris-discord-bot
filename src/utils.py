import hikari
import re

from src import api

def extract_game_link_id(msg: hikari.Message) -> str:
    #Extract game link ID from message content.
    match = re.search(r'https://solaris\.games/#/game(?:/detail)?\?id=(\w+)', msg.content, re.IGNORECASE)

    if match and match.group(1):
        return match.group(1)  # Return the captured game link ID

    return None

def get_base_embeded_response() -> hikari.Embed:
    #Create a base embed response.
    return (hikari.Embed()
            .set_author(name="Solaris", url="https://solaris.games"))

async def try_auto_game_link(msg: hikari.Message):
    game_id = extract_game_link_id(msg)

    if game_id is None:
        return
    
    game_info = api.get_game_info(game_id)
    game_name, game_type, game_players, game_description, game_mode = get_game_text(game_info)


    #Build embed
    embed = get_base_embeded_response()
    embed.url = f"https://solaris.games/#/game/detail?id={str(game_id)}"
    embed.description = game_description
    embed.title = game_name
    embed.add_field("Mode", game_mode, inline=True)
    embed.add_field("Type", game_type, inline=True)
    embed.add_field("Players", game_players, inline=True)

    await msg.respond(embed)



def get_game_text(game_info):
    game_name = game_info['settings']['general']['name']
    game_type = get_game_type_friendly_text(game_info)
    game_players = f"{game_info['state']['players']} / {game_info['settings']['general']['playerLimit']}"
    game_description = game_info['settings']['general']['description']
    game_mode = get_game_mode_friendly_text(game_info)


    return game_name, game_type, game_players, game_description, game_mode

def get_game_type_friendly_text(game_info):
    game_type_map = {
        'tutorial': 'Tutorial',
        'new_player_rt': 'New Players',
        'standard_rt': 'Standard',
        'standard_tb': 'Standard - TB',
        '1v1_rt': '1 vs. 1',
        '1v1_tb': '1 vs. 1 - TB',
        '32_player_rt': '32 Players',
        'custom': 'Custom',
        'special_dark': 'Dark Galaxy',
        'special_ultraDark': 'Ultra Dark Galaxy',
        'special_orbital': 'Orbital',
        'special_battleRoyale': 'Battle Royale',
        'special_homeStar': 'Capital Stars',
        'special_homeStarElimination': 'Elimination',
        'special_anonymous': 'Anonymous',
        'special_kingOfTheHill': 'King Of The Hill',
        'special_tinyGalaxy': 'Tiny Galaxy',
        'special_freeForAll': 'Free For All',
        'special_arcade': 'Arcade'
    }

    return game_type_map.get(game_info['settings']['general']['type'], 'Unknown')

def get_game_mode_friendly_text(game_info):
    game_mode_map = {
        'conquest': 'Conquest',
        'battleRoyale': 'Battle Royale',
        'kingOfTheHill': 'King of the Hill'
    }

    return game_mode_map.get(game_info['settings']['general']['mode'], 'Unknown')