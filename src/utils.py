import hikari
import re

def extract_game_link_id(msg: hikari.Message) -> str:
    #Extract game link ID from message content.
    match = re.search(r'https://solaris\.games/#/game(?:/detail)?\?id=(\w+)', msg.content, re.IGNORECASE)

    if match and match.group(1):
        return match.group(1)  # Return the captured game link ID

    return None

def get_base_embeded_response() -> hikari.Embed:
    #Create a base embed response.
    return (hikari.Embed()
            .set_url("https://solaris.games")
            .set_author(name="Solaris"))