import keyboard
from datetime import datetime
from modules.utils import format_elapsed_time

verbose = False
TOGGLE_RECORD_SHORTCUT = "alt+F9"
is_recording = False
recording_start_time = None

def start_capture():
    global is_recording, recording_start_time

    if is_recording:
        stop_capture()

    keyboard.send(TOGGLE_RECORD_SHORTCUT)
    is_recording = True
    recording_start_time = datetime.now()

    timestamp = _get_timestamp()
    print(f"[{timestamp}] : Starting Capture")

def stop_capture():
    global is_recording, recording_start_time

    if not is_recording:
        return
    
    keyboard.send(TOGGLE_RECORD_SHORTCUT)
    is_recording = False

    #TODO: Need to check if recording_start_time is None
    elapsed_time_secs = (datetime.now() - recording_start_time).total_seconds()
    recording_start_time = None

    timestamp = _get_timestamp()
    elapsed_time_human = format_elapsed_time(elapsed_time_secs)
    print(f"[{timestamp}] : Ending Capture : {elapsed_time_human}")

def _get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")