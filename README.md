# Flow.Launcher.Plugin.Gitmoji

A Flow Launcher plugin to search and copy the right Gitmoji into your clipboard

![Alt text](image.png)

## Requirements

To use Python plugins within Flow you'll need Python 3.8 or later installed on your system. You also may need to select your Python installation directory in the Flow Launcher settings. As of v1.8, Flow Launcher should take care of the installation of Python for you if it is not on your system.

## Installing
The Plugin has not been officially added to the supported list of plugins. 

You can also manually add it.

## Manual
Add the plugins folder to %APPDATA%\Roaming\FlowLauncher\Plugins\ and run the Flow command ```restart Flow Launcher```.

## Python Package Requirements
This plugin automatically packs the required packages during release so for normal usage in Flow, no additional actions are needed.

If you would like to manually install the packages:

This plugin depends on the python flowlauncher package.

Without this package installed in your python environment the plugin wont work!

The easiest way to install it is to open a CLI like Powershell, navigate into the plugins folder and run the following command:

``` pip install -r requirements.txt -t ./lib ```

## Usage
Simply type ```gm``` to start searching Gitmoji.
You can filter Gitmoji by typing the name or a word in the description.

Then select the Gitmoji you want in to copy to the clipboard.


## Thanks

This plugin were not possible without : 

https://github.com/carloscuesta/gitmoji

https://github.com/Garulf/Emoji-plus