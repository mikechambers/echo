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


from enum import Enum
class Mode(Enum):
    NONE = 0
    STORY = 2
    STRIKE = 3
    RAID = 4
    ALL_PVP = 5
    PATROL = 6
    ALL_PVE = 7
    CONTROL = 10
    CLASH = 12
    RESERVED13 = 13
    CRIMSON_DOUBLES = 15
    NIGHTFALL = 16
    HEROIC_NIGHTFALL = 17
    ALL_STRIKES = 18
    IRON_BANNER = 19
    ALL_MAYHEM = 25
    SUPREMACY = 31
    PRIVATE_MATCHES_ALL = 32
    SURVIVAL = 37
    COUNTDOWN = 38
    SOCIAL = 40
    TRIALS_COUNTDOWN = 41
    TRIALS_SURVIVAL = 42
    IRON_BANNER_CONTROL = 43
    IRON_BANNER_CLASH = 44
    IRON_BANNER_SUPREMACY = 45
    SCORED_NIGHTFALL = 46
    SCORED_HEROIC_NIGHTFALL = 47
    RUMBLE = 48
    ALL_DOUBLES = 49
    DOUBLES = 50
    PRIVATE_MATCHES_CLASH = 51
    PRIVATE_MATCHES_CONTROL = 52
    PRIVATE_MATCHES_SUPREMACY = 53
    PRIVATE_MATCHES_COUNTDOWN = 54
    PRIVATE_MATCHES_SURVIVAL = 55
    PRIVATE_MATCHES_MAYHEM = 56
    PRIVATE_MATCHES_RUMBLE = 57
    HEROIC_ADVENTURE = 58
    SHOWDOWN = 59
    LOCKDOWN = 60
    SCORCHED = 61
    SCORCHED_TEAM = 62
    GAMBIT = 63
    ALL_PVE_COMPETITIVE = 64
    BREAKTHROUGH = 65
    BLACK_ARMORY_RUN = 66
    SALVAGE = 67
    IRON_BANNER_SALVAGE = 68
    PVP_COMPETITIVE = 69
    PVP_QUICKPLAY = 70
    CLASH_QUICKPLAY = 71
    CLASH_COMPETITIVE = 72
    CONTROL_QUICKPLAY = 73
    CONTROL_COMPETITIVE = 74
    GAMBIT_PRIME = 75
    RECKONING = 76
    MENAGERIE = 77
    VEX_OFFENSIVE = 78
    NIGHTMARE_HUNT = 79
    ELIMINATION = 80
    MOMENTUM = 81
    DUNGEON = 82
    SUNDIAL = 83
    TRIALS_OF_OSIRIS = 84
    DARES = 85
    OFFENSIVE = 86
    LOST_SECTOR = 87
    RIFT = 88
    ZONE_CONTROL = 89
    IRON_BANNER_RIFT = 90
    IRON_BANNER_ZONE_CONTROL = 91
    RELIC = 92


    def __str__(self):
        return self.name
    
    @classmethod
    def from_string(cls, value):
        try:
            return cls[value.upper()]  # Convert input to uppercase and match Enum
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid input '{value}'. Please provide a valid mode.") from e
