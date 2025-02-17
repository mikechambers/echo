# echo

echo is a Python3 script that tracks Destiny 2 game play and automatically creates recordings of the specified game mode using [NVIDIA Shadowplay](https://www.nvidia.com/en-ph/geforce/geforce-experience/shadowplay/) or [Steam Game Recording](https://store.steampowered.com/gamerecording).

For example, you could have it automatically start recording when you start a PVP match, and end it when the match is over.

If you run into any issues, have any ideas, or just want to chat, please post in [issues](https://github.com/mikechambers/echo/issues) or share on [Discord](https://discord.gg/2Y8bV2Mq3p).

## Requirements

This script requires that:

-   Python 3 is installed
-   NVIDIA Shadowplay or Stream Game Recording is installed and enabled
-   You have a valid Destiny 2 Developer API Key. You can grab one from the [Bungie Developer Portal](https://www.bungie.net/en/User/API)

## Installation

The script requires Python3 and a number of libraries to be installed. You can install the required libraries with:

```bash
pip install -r requirements.txt
```

## Usage

Basic usage to automatically create a video for every (non-private) PVP match:

```bash
python3 echo.py --mode all_pvp --bungie-id mesh#3230 --api-key XXXXXXXXXXXXXXXXXXXXX
```

The video clip will be saved in the default directory for NVIDIA Shadowplay clips.

Note, if the API key is not specified via the command line, the script will look for it in an environment variable named DESTINY_API_KEY.

By default, it uses the ALT-F9 keyboard shortcut to toggle video recording (the default for Shadowplay). You can change this via the _--keyboard-shortcut_ argument when calling the script.

By default, the script uses the keyboard shortcut for NVIDIA Shadowplay. If you are using Steam Game Recording, then specify the keyboard shortcut to enable it (by default _CTRL+F11_)

```bash
python3 echo.py --mode all_pvp --bungie-id mesh#3230 --api-key XXXXXXXXXXXXXXXXXXXXX --keyboard-shortcut "CTRL+F11"
```

You can find a complete list of options by running:

```bash
python3 echo.py --help
```

## Known Issues

This is a first beta, so there are a lot of rough edges. Error handing on API calls is basic, so if something goes wrong (especially with the API), there will not be detailed info yet.

If the script starts recording, and you manually stop recording, the script may no longer work (it won't know the status of recording).

## Questions, Feature Requests, Feedback

If you have any questions, feature requests, need help, or just want to chat, you can ask on the [Discord](https://discord.gg/2Y8bV2Mq3p) as well as ping me on [Twitter](https://twitter.com/mesh) or via email at [mikechambers@gmail.com](mailto:mikechambers@gmail.com).

You can also log bugs and feature requests on the [issues page](https://github.com/mikechambers/echo/issues).

## License

Project released under a [MIT License](LICENSE.md).

[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE.md)
