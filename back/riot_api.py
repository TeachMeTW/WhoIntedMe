import requests
import os
from dotenv import load_dotenv

load_dotenv()

RIOT_API_KEY = os.getenv("RIOT_API_KEY")


def get_user(username):
    """Fetch user details from the Riot API using the given username.

    Args:
    - username (str): The username of the user whose details are to be fetched.

    Returns:
    - dict: A dictionary containing user details.

    Raises:
    - Exception: If the API request fails.
    - KeyError: If the expected 'id' key is not found in the API response.
    """

    response = requests.get(
        f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}?api_key={RIOT_API_KEY}"
    )
    if response.status_code != 200:
        raise Exception("API request failed")

    data = response.json()
    if "id" not in data:
        raise KeyError("Key 'id' not found in API response")

    return data


def recent_match_ids(puuid):
    """Fetch recent match IDs for a given user puuid from the Riot API.

    Args:
    - puuid (str): The unique identifier for the user.

    Returns:
    - list: A list of match IDs.

    Raises:
    - Exception: If the API request fails or if the response isn't a list.
    """

    response = requests.get(
        f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={RIOT_API_KEY}"
    )
    if response.status_code != 200:
        raise Exception("API request failed")

    data = response.json()
    if not isinstance(data, list):
        raise Exception("Expected a list of matches from API")

    return data


def match_data(match):
    """Fetch match details for a given match ID from the Riot API.

    Args:
    - match (str): The unique identifier for the match.

    Returns:
    - dict: A dictionary containing match details.

    Raises:
    - Exception: If the API request fails.
    - KeyError: If expected keys are not found in the API response.
    """

    response = requests.get(
        f"https://americas.api.riotgames.com/lol/match/v5/matches/{match}?api_key={RIOT_API_KEY}"
    )
    if response.status_code != 200:
        raise Exception("API request failed")

    data = response.json()
    expected_keys = ["metadata", "info"]
    for key in expected_keys:
        if key not in data:
            raise KeyError(f"Expected key {key} not found in API response")

    return data


def get_single_match(username):
    """Fetch the most recent match details for a given username.

    Args:
    - username (str): The username of the user.

    Returns:
    - dict: A dictionary containing match details combined from metadata and info.
    """

    recent = match_data(recent_match_ids(get_user(username)["puuid"])[0])
    participants_data = recent.get("metadata", {}).get("participants", [])
    info_data = recent.get("info", {})

    # Combine 'participants' with 'info'
    combined_data = {"participants": participants_data, **info_data}
    return combined_data


def get_all_matches(username):
    """Fetch all match details for a given username.

    Args:
    - username (str): The username of the user.

    Returns:
    - list: A list of dictionaries, each containing match details.
    """

    match_ids = recent_match_ids(get_user(username)["puuid"])
    all_matches = []

    for match_id in match_ids:
        match_details = match_data(match_id)

        participants_data = match_details.get("metadata", {}).get("participants", [])

        info_data = match_details.get("info", {})

        # Combine 'participants' with 'info'
        combined_data = {"participants": participants_data, **info_data}
        all_matches.append(combined_data)

    return all_matches
