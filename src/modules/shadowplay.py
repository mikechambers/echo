import keyboard


verbose = False
TOGGLE_RECORD_SHORTCUT = "alt+F9"
is_recording = False
def start_capture():
    global is_recording, verbose

    if is_recording:
        stop_capture()

    keyboard.send(TOGGLE_RECORD_SHORTCUT)
    is_recording = True

    if verbose:
        print("Starting Capture")

def stop_capture():
    global is_recording, verbose

    if is_recording:
        keyboard.send(TOGGLE_RECORD_SHORTCUT)
        is_recording = False

        if verbose:
            print("Stopping Capture")