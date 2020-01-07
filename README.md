# HRI20-Not-Some-Random-Agent-Personalizing-Service-Robot

COPYRIGHT(C) 2020 - Carnegie Mellon University - Code released under MIT. Contact: Sam - sreig@cs.cmu.edu 

This repository contains the following elements related to the user enactments study described in the HRI 2020 paper: "Not Some Random Agent: Multi-person Interaction with a Personalizing Service Robot":

1. Code to run the wizarding interface, which allows for generating audio files for the agents' utterances from a set of scripts and for creating new utterances
2. The interview protocol

The voices used in the study are from Google Cloud Services. You must have Google Cloud credentials to use them. 

### User enactments wizard interface

_How we created audio files of different agents' lines from prewritten scenario scripts for study on interactions between multiple co-embodied agents and users in services settings._

Two ways to create audio files in specified agent's voice:
1. _texttospeechwizard.py_: 
Creates robot audio files for any scenario(s) entered at the command line from downloaded folder of scripts (clinic, store, hotel)

2. _interface.py_:
Creates audio file for input line and specified agent
<br />

Initial setup:
1. Download project.
2. Set up a [Python development environment](https://cloud.google.com/python/setup).
3. Install necessary packages: tkinter, pyglet, google.cloud, playsound, docx2txt, os.
4. Create the scripts for each environment (clinic, store, hotel) folder. Add them to a folder called "scripts", with subfolders for each environment (clinic, store, hotel). The robot's dialogue in the scripts must be formatted like this:<br />
    Robot line in script format: 
    > Robot (AGENT_NAME): This is what the robot says.
<br />
This specific format is used by texttospeechwizard.py to parse the script for lines of robot dialogue audio from which to create audio files.

Before running _texttospeechwizard.py_ or _interface.py_:
1. Open new Terminal window.
2. Enter Python virtual environment.<br />
    ```
    source env/bin/activate
    ```
3. Enter Google application credentials.<br />
    ```
    export GOOGLE_APPLICATION_CREDENTIALS="[FILE_NAME].json"
    ```
<br />

To create audio files from prewritten scripts:
1. Run _texttospeechwizard.py_ with specified command line arguments:<br />
    ```
    python3 texttospeechwizard.py PARTICIPANT_1 PARTICIPANT_2 "context_letter + config_num" "context_letter + config_num" ...
    ```
    The numbers for config_num are: 1 for singular agent, 2 for personal service agent, 3 for life agent. For example, to create all audio files for participants Alex and Taylor, for session order clinic - singular agent, store - personal service agent, hotel - life agent:<br />
    ```
    python3 texttospeechwizard.py Alex Taylor c1 s2 h3
    ```
Audio files created and organized in soundfiles subfolder.
<br />

To create one audio file at a time:
1. Run _interface.py_:<br />
    ```
    python3 interface.py
    ```
2. Enter text into text box and choose agent voice.
3. Click "Make audio file". Audio file plays out loud, Audio files generated in soundfiles folder.
<br />

Agent voices:
* Alpha (Singular Agent)
* Moon and Saturn (Personal Service Agent)
* Basil and Sunflower (Life Agent)

[Google WaveNet voices](https://cloud.google.com/text-to-speech/docs/voices) can be changed in _texttospeechwizard.py_


### Interview protocol

The semi-structured interview questions are in a pdf file in this repository. 