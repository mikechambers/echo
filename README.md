# echo

echo is a Python3 script that tracks Destiny 2 game play and automatically creates clips of the specified game mode using NVIDIA Shadowplay.

For example, you could have it automatically start recording when you start a PVP match, and end it when the match is over.

## Requirements

This script requires that:

-   Python 3 is installed
-   NVIDIA Shadowplay is installed and enabled
-   The keyboard shortcut to toggle recording is ALT-F9
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

Note, if the API key is not specified via the command line, the script will look for it in an environment variable named DESTINY_API_KEY

You can find a complete list of options by running:

```bash
python3 echo.py --help
```

## Known Issues

This is a first beta, so there are a lot of rouch edges. Error handing on API calls is basic, so if something goes wrong (especially with the API), there will not be detailed info yet.

## Questions, Feature Requests, Feedback

If you have any questions, feature requests, need help, or just want to chat, you can ping me on [Twitter](https://twitter.com/mesh) or via email at [mikechambers@gmail.com](mailto:mikechambers@gmail.com).

You can also log bugs and feature requests on the [issues page](https://github.com/mikechambers/echo/issues).

## License

Project released under a [MIT License](LICENSE.md).

[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE.md)
