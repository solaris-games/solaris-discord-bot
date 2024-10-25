import os
import requests

def get(url: str):
    base_url = os.getenv("SOLARIS_API_BASE_URL")
    response = requests.get(f"{base_url}/{url}")

    if response.status_code != 200:
        print(response.json())  # Print error details for debugging
        raise Exception(f"GET {url} failed with status {response.status_code}.")
    
    return response.json()

def get_bans():
    return get("game/specialists/bans")

def get_flux():
    return get("game/flux")

def get_game_info(game_id: str):
    return get(f"game/{game_id}/info")

def get_global_leaderboard():
    return get("user/leaderboard?limit=10&sortingKey=rank")

def get_elo_leaderboard():
    return get("user/leaderboard?limit=10&sortingKey=elo-rating")

def get_guild_leaderboard():
    return get("guild/leaderboard?limit=10&sortingKey=totalRank")