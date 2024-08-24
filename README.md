# Flow.Launcher.Plugin.Gitmoji

[![GitHub release](https://img.shields.io/github/release/Galedrim/Flow.Launcher.Plugin.Gitmoji)]()
[![GitHub latest commit](https://badgen.net/github/last-commit/Galedrim/Flow.Launcher.Plugin.Gitmoji)]()
[![Github All Releases](https://img.shields.io/github/downloads/Galedrim/Flow.Launcher.Plugin.Gitmoji/total.svg)]()

This Flow Launcher plugin allows you to efficiently search for and copy the appropriate Gitmoji to your clipboard. 
Each Gitmoji comes with a detailed description and an example of its usage, making it easier to incorporate these emojis into your commit messages accurately.

![image](https://github.com/user-attachments/assets/e1d937e8-87a5-45db-8816-82d67792fbbd)

## Requirements

To use Python plugins within Flow-Launcher, you'll need Python 3.11 or later installed on your system. You also may need to select your Python installation directory in the Flow Launcher settings. As of v1.8, Flow Launcher should take care of the installation of Python for you if it is not on your system.

## Installing
The Plugin has been officially added to the supported list of plugins. 
Run the command  ```pm install gitmoji``` to install it.

You can also manually add it.

## Manual
Add the plugins folder to %APPDATA%\Roaming\FlowLauncher\Plugins\ and run the Flow command ```restart Flow Launcher```.

## Python Package Requirements
This plugin automatically packs the required packages during release so for regular usage in Flow, no additional actions are needed.

If you would like to manually install the packages:

This plugin depends on the Python flow-launcher package.

Without this package installed in your Python environment the plugin won't work!

The easiest way to install it is to open a CLI like Powershell, navigate into the plugins folder and run the following command:

``` pip install -r requirements.txt -t ./lib ```

## Usage
Type ```gm``` to start searching Gitmoji.
You can filter Gitmoji by typing the name or a word in the description.

Then select the Gitmoji you want to copy to the clipboard.
