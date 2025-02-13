import hikari
import re
import random

from src import api
from dataclasses import dataclass
from dataclasses import field

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

def get_spec_names(spec_type):
    if spec_type == "carrier":
        specs = api.get_carrier_specs()
    if spec_type == "star":
        specs = api.get_star_specs()

    names = [spec['name'] for spec in specs]

    return names

def get_spec_details(name, spec_type):
    if spec_type == "carrier":
        specs = api.get_carrier_specs()
    if spec_type == "star":
        specs = api.get_star_specs()
    
    for spec in specs:
        if spec['name'] == name:
            image_url = f"src/assets/specialist/{spec['key']}.png"
            description = spec['description']
            base_cost_credits = spec['baseCostCredits']
            base_cost_specialist_credit = spec['baseCostCreditsSpecialists']

            return image_url, description, base_cost_credits, base_cost_specialist_credit
        
    else: 
        return None
    
def filter_choices(items: list, option: hikari.AutocompleteInteractionOption)-> list:
    filtered_items = [item for item in items if option.value.lower() in item.lower()]
  
    # Limit the number of choices based on the filtered items
    choices = [{"name": item, "value": item} for item in filtered_items[:25]]

    if not filtered_items:
        return []
    else: 
        return [f['name'] for f in choices]

@dataclass
class DiceHandler():
    die_count: int
    die_size: int
    mod: int = 0
    result: int = 0
    final_result: int = 0
    dropped_roll: int = 0
    rolls: list = field(default_factory=list)

    def roll_dice(self):
        for roll in range(self.die_count):
            rolled = random.randrange(1, self.die_size)
            self.final_result += rolled
            self.rolls.append(rolled)

    def roll_die_consider_adv(self, mod, roll_twice=None):
        self.mod = mod
        if roll_twice:
            die_count = 2
        else:
            die_count = 1
        
        for roll in range(die_count):
            result = random.randrange(1, self.die_size)
            self.result += result
            self.rolls.append(result)
        
        if roll_twice == "Advantage":
            result = self.get_highest_roll()
        if roll_twice == "Disadvantage":
            self.result = self.get_lowest_roll()
        
        self.final_result = self.result + mod
    
    def get_highest_roll(self):
        highest_roll = max(self.rolls)
        self.dropped_roll = min(self.rolls)
        return highest_roll
    
    def get_lowest_roll(self):
        lowest_roll = min(self.rolls)
        self.dropped_roll = max(self.rolls)
        return lowest_roll


def map_die_type_to_int(die_type: str) -> int:
    die_map = {
        'd2': 2,
        'd4': 4,
        'd6': 6,
        'd8': 8,
        'd10': 10,
        'd12': 12,
        'd20': 20,
        'd100': 100
    }

    return die_map.get(die_type)