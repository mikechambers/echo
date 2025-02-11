import requests
from datetime import datetime, timezone
import random


api_key = "8c84b6c7a153461fac699e2ab24283e7"
user_agent = "echo"

PROFILE_URL_TEMPLATE = ""

HEADERS_TEMPLATE = {
    "X-API-Key": f"{api_key}",
    "User-Agent": f"{user_agent}",
}

_headers = None

_mostRecentProfileData = None

# this assumes api_key is set once before any API calls
def _get_headers():
    global api_key, user_agent, _headers

    if api_key == None:
        raise APIKeyNotSetError("API Key Not Set")

    if _headers == None:
        _headers = HEADERS_TEMPLATE

    return _headers

def retrieve_current_activity_modes():
    profile = retrieve_profile()

    character = find_most_recent_character(profile)

    mode = profile["Response"]["characterActivities"]["data"][character["id"]].get("currentActivityModeTypes", [])

    return mode

    

def find_most_recent_character(profile):
    characters = profile["Response"]["characters"]["data"]

    mostRecentCharacter = None
    for key in characters:
        d = datetime.strptime(characters[key]["dateLastPlayed"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

        character = {
            "id":key,
            "dateLastPlayed":d
        }

        if mostRecentCharacter == None or character["dateLastPlayed"] > mostRecentCharacter["dateLastPlayed"]:
                mostRecentCharacter = character
    
    return mostRecentCharacter




def retrieve_profile():
    global _mostRecentProfileData

    rnd = random.randint(10000, 10000000)
    url = f"https://www.bungie.net/Platform/Destiny2/1/Profile/4611686018429783292/?components=200,204,1000&rnd={rnd}"
    data = retrieve_json(url)

    d = datetime.strptime(data["Response"]["responseMintedTimestamp"], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)

    #d = datetime.strptime(data["Response"]["responseMintedTimestamp"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

    if _mostRecentProfileData == None or d > _mostRecentProfileData["responseMintedTimestamp"]:
        _mostRecentProfileData = {
            "data":data,
            "responseMintedTimestamp":d
        }

    return _mostRecentProfileData["data"]

def retrieve_json(url):

    headers = _get_headers()
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise APIResponseError(f"Error retrieving URL : {response.status_code}: {response.text}")

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        raise APIResponseError("Error parsing JSON response")

    return data


class APIKeyNotSetError(Exception):
    pass

class APIResponseError(Exception):
    pass