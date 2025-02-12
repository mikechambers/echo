import sys
import os
import argparse
from modules import shadowplay
from modules import destiny
from modules.mode import Mode
import time

API_KEY_ENV_NAME = "DESTINY_API_KEY"

verbose = False


mode = None
last_modes = []

api_key = None

def main():
    global verbose, last_modes, api_key

    shadowplay.verbose = verbose
    destiny.api_key = api_key
    destiny.verbose = verbose

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
        type=str,
        help="Bungie ID (NAME#ID) for the account to track (will automatically track the last played character)",
        required = True
    )

    parser.add_argument(
        "--api-key",
        type=str,
        help=f"API Key for authentication. Must be set via argument, or environment variables [{API_KEY_ENV_NAME}]")
    
    
    args = parser.parse_args()

    api_key = _get_arg_from_env_or_error(API_KEY_ENV_NAME, args.api_key, "--api-key")

    verbose = args.verbose
    mode = args.mode
    
    try:
        main()
    except Exception as e:
        print(f"An error occurred. Aborting : {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

