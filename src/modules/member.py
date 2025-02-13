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

import re

class Member:
    def __init__(self, membership_id: str, platform_id: int):
        self.membership_id = membership_id
        self.platform_id = platform_id

    def __repr__(self):
        return f"Member(membership_id='{self.membership_id}', platform_id={self.platform_id})"

class BungieId:
    def __init__(self, name: str = "", code: str = ""):
        """Initialize a BungieId instance."""
        self.name = name
        self.code = code

    @classmethod
    def from_string(cls, bungie_id: str):
        """Create BungieId from a string like 'Name#1234'."""
        if not bungie_id:
            return cls()

        id_pieces = bungie_id.split("#")

        if len(id_pieces) < 2:
            return cls(name=bungie_id)

        code = id_pieces.pop()
        name = "#".join(id_pieces)

        return cls(name=name, code=code)

    @staticmethod
    def parse_code(code):
        """Convert an integer code into a zero-padded string of length 4."""
        if isinstance(code, int):
            return f"{code:04d}"
        return ""

    @property
    def is_valid(self):
        """Check if BungieId is valid (non-empty name and 4-digit numeric code)."""
        return bool(self.name and re.fullmatch(r"\d{4}", self.code))

    def __str__(self):
        """String representation of BungieId."""
        return f"{self.name}#{self.code}"

    def __repr__(self):
        """Debug representation of BungieId."""
        return f"BungieId(name='{self.name}', code='{self.code}')"

    def __eq__(self, other):
        """Equality check."""
        if not isinstance(other, BungieId):
            return False
        return self.name == other.name and self.code == other.code

    def __hash__(self):
        """Hash method to make the object hashable."""
        return hash((self.name, self.code))
