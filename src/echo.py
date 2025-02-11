import sys
import argparse
from modules import shadowplay
from modules import destiny
from modules.mode import Mode
import time


verbose = False


mode = None
last_modes = []
def main():
    global verbose, last_modes

    shadowplay.verbose = verbose

    print("Watching for mode changes...")
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

    args = parser.parse_args()
    verbose = args.verbose
    mode = args.mode
    
    try:
        main()
    except Exception as e:
        print(f"An error occurred. Aborting : {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)