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

import sys
import os
import argparse
from modules import shadowplay
from modules.destiny import Destiny
from modules.member import BungieId
from modules.mode import Mode
import time

VERSION = "0.85.1"
API_KEY_ENV_NAME = "DESTINY_API_KEY"

verbose = False

mode = None
last_modes = []

api_key = None
bungie_id = None

def main():
    global verbose, last_modes, api_key, bungie_id

    shadowplay.verbose = verbose

    destiny = Destiny(api_key, verbose)

    member = destiny.retrieve_member(bungie_id)
    print(member)

    print(f"Watching for {mode.name} changes...")
    while True:
        modes = destiny.retrieve_current_activity_modes()

        if mode.value in modes and mode.value not in last_modes:
            shadowplay.start_capture()
        elif mode.value not in modes and mode.value in last_modes:
            shadowplay.stop_capture()

        last_modes = modes

        #if mode != lastMode:
        #    print(f"Modes Changed: {modes}")
        #    lastMode = mode
        time.sleep(2)


def _parse_bungie_id(value: str) -> BungieId:
    """Parses and validates the Bungie ID, returning a BungieId object"""
    bungie_id = BungieId.from_string(value)
    if not bungie_id.is_valid:
        raise argparse.ArgumentTypeError(
            "Invalid Bungie ID format. Expected format: NAME#1234 (e.g., Guardian#1234)"
        )
    return bungie_id  # Return the actual BungieId object

def _get_arg_from_env_or_error(env_var, arg_value, arg_name):
    """Return argument value, fallback to environment variable, else throw an error."""
    if arg_value is not None:
        return arg_value
    elif env_var in os.environ:
        return os.environ[env_var]
    else:
        print(f"Error: {arg_name} is required either as an argument or in environment variable {env_var}.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Automate Destiny 2 Video clip capture with NVIDIA ShadowPlay"
    )

    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {VERSION}',
        help="Display the version")

    parser.add_argument(
        '--verbose',
        dest='verbose', 
        action='store_true', 
        help='display additional information as script runs'
    )

    parser.add_argument(
        "--mode",
        type=Mode.from_string,
        choices=list(Mode),
        help="Game mode to record.",
        required=True)
    
    parser.add_argument(
        "--bungie-id",
        type=_parse_bungie_id,  # Parse directly into a BungieId object
        help="Bungie ID (NAME#ID) for the account to track (e.g., Guardian#1234)",
        required=True,
    )

    parser.add_argument(
        "--api-key",
        type=str,
        help=f"API Key for authentication. Must be set via argument, or environment variables [{API_KEY_ENV_NAME}]")
    
    
    args = parser.parse_args()

    api_key = _get_arg_from_env_or_error(API_KEY_ENV_NAME, args.api_key, "--api-key")

    verbose = args.verbose
    mode = args.mode
    bungie_id = args.bungie_id

    try:
        main()
    except Exception as e:
        print(f"An error occurred. Aborting : {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

