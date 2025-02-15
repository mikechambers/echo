# Copyright (c) 2025 Mike Chambers
# https://github.com/mikechambers/echo
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import requests
from dateutil import parser
import random
from modules.member import BungieId, Member

class Destiny:

    def __init__(self, api_key: str, verbose: bool = False):
        self.api_key = api_key
        self.verbose = verbose
        self._mostRecentProfileData = None
        self._headers = None
        self._user_agent = "echo"

    def retrieve_member(self, bungie_id:BungieId):
        url = "https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayerByBungieName/-1/"

        data = {
            "displayName": bungie_id.name,
            "displayNameCode": bungie_id.code
        }

        if self.verbose:
            print(f"retrieve_member : {url}")
        
        # Send the POST request
        response_data = self.retrieve_json_post(url, data)

        cards = response_data["Response"]

        if not cards:
            return None
        
        if len(cards) == 1:
            return Member(cards[0]["membershipId"], cards[0]["membershipType"])

        crosssave_disable_found = False
        crosssave_override_id = 0

        for card in cards:
            override = card["crossSaveOverride"]

            if override == 0:
                crosssave_disable_found = True
                continue
            else:
                crosssave_override_id = override

        out = None
        card = cards.pop(0)
        if not crosssave_disable_found:
            for c in cards:
                if c["crossSaveOverride"] == 0 or c["membershipType"] == crosssave_override_id:
                    card = c

            out = card

        else:
            profiles = self.retrieve_linked_profiles(card["membershipId"], card["membershipType"])

            if not profiles:
                return None
            
            most_recent = profiles.pop(0)
            most_recent_date = parser.isoparse(most_recent["dateLastPlayed"])

            for profile in profiles:
                last_played_date = parser.isoparse(profile["dateLastPlayed"])

                most_recent = profile
                most_recent_date = last_played_date

            out = most_recent

        return Member(out["membershipId"], out["membershipType"])

    def retrieve_linked_profiles(self, membership_id:str, platform_id:int) -> dict:
        url = f"https://www.bungie.net/Platform/Destiny2/{platformId}/Profile/{membership_id}/LinkedProfiles"

        response = self.retrieve_json_get(url)

        return response["Response"]["profiles"]

    # this assumes api_key is set once before any API calls
    def _get_headers(self):

        if self.api_key == None:
            raise APIKeyNotSetError("API Key Not Set")

        if self._headers == None:
            self._headers = {
                "X-API-Key": f"{self.api_key}",
                "User-Agent": f"{self._user_agent}",
            }

        return self._headers

    def retrieve_current_activity_modes(self):
        profile = self.retrieve_profile()

        character = self.find_most_recent_character(profile)

        mode = profile["Response"]["characterActivities"]["data"][character["id"]].get("currentActivityModeTypes", [])

        return mode

        

    def find_most_recent_character(self, profile):
        characters = profile["Response"]["characters"]["data"]

        mostRecentCharacter = None
        for key in characters:
            #d = datetime.strptime(characters[key]["dateLastPlayed"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            d = parser.isoparse(characters[key]["dateLastPlayed"])

            character = {
                "id":key,
                "dateLastPlayed":d
            }

            if mostRecentCharacter == None or character["dateLastPlayed"] > mostRecentCharacter["dateLastPlayed"]:
                    mostRecentCharacter = character
        
        return mostRecentCharacter


    def retrieve_profile(self):

        rnd = random.randint(10000, 10000000)
        url = f"https://www.bungie.net/Platform/Destiny2/1/Profile/4611686018429783292/?components=200,204,1000&rnd={rnd}"

        if self.verbose:
            print(f"retrieve_profile : {url}")

        data = self.retrieve_json_get(url)

        d = parser.isoparse(data["Response"]["responseMintedTimestamp"])

        if self._mostRecentProfileData == None or d > self._mostRecentProfileData["responseMintedTimestamp"]:
            self._mostRecentProfileData = {
                "data":data,
                "responseMintedTimestamp":d
            }

        return self._mostRecentProfileData["data"]

    def parse_response(self, response):
        if response.status_code != 200:
            raise APIResponseError(f"Error retrieving URL : {response.status_code}: {response.text}")

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            raise APIResponseError("Error parsing JSON response")
        
        return data

    def retrieve_json_post(self, url, data):

        headers = self._get_headers()
        response = requests.post(url, json=data, headers=headers)

        return self.parse_response(response)

    def retrieve_json_get(self, url:str):

        headers = self._get_headers()
        response = requests.get(url, headers=headers)

        return self.parse_response(response)
    
class APIKeyNotSetError(Exception):
    pass

class APIResponseError(Exception):
    pass