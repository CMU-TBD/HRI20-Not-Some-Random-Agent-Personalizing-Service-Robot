#!/usr/bin/env python

# Copyright 2018 Google Inc. All Rights Reserved.
# Modifications Copyright (c) 2019 Sam Reig & Janet Wang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Creates all audio files for any scenario(s) entered at the command line using Google Cloud Text-To-Speech API.
     Example usage: python3 texttospeechwizard.py Janet Sam c1 s2 h3
                    ( = clinic singular, store psa, hotel my) """

# enter Python virtual environment: source env/bin/activate
# enter GOOGLE_APPLICATION_CREDENTIALS: export GOOGLE_APPLICATION_CREDENTIALS="wizardassistant-f50eed8611aa.json"

import sys
import tkinter
import pyglet
from google.cloud import texttospeech
from playsound import playsound
import docx2txt
import os

# Alpha = Singular Service Agent
# Moon/Saturn = Personal Service Agent
# Basil/Sunflower = My Agent
agent_names = ["ALPHA", "MOON", "SATURN", "BASIL", "SUNFLOWER"]

fromFile = False # from interface

# create audio file from input text using specified agent's voice
def make_audio_file(phrase, agent, scenario=""):
    # instantiate client
    client = texttospeech.TextToSpeechClient()

    # set synthesized speech parameters
    input_text = texttospeech.types.SynthesisInput(text=phrase)
    voice = create_voice(agent)
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # perform text-to-speech request on input text w selected voice parameters and audio file type
    response = client.synthesize_speech(input_text, voice, audio_config)

    # set path to audio file
    audio_file_name = set_audio_name(phrase, agent, scenario)
    if (fromFile): # in participants -> scenario folders
        path = 'soundfiles/' + participant_1 + "_" + participant_2 + "/"  + scenario + "/" + audio_file_name
    else: # input text from interface, goes directly to soundfiles folder
        path = "soundfiles/" + audio_file_name

    # write the response to the output file.
    with open(path, 'wb') as out:
        out.write(response.audio_content) # The response's audio_content is binary
        print('Audio written to file \"' + audio_file_name + '\"' )

    # play audio if input text from interface
    if (not fromFile):
        playsound(path)

# define values of parameters for voice based on agent/agent config (Wavenet)
def create_voice(agent):
    if agent == agent_names[0]: # Alpha
        voice_lang = "en-US"
        voice_name = "en-US-Wavenet-A"
        voice_gender = texttospeech.enums.SsmlVoiceGender.NEUTRAL
    elif agent == agent_names[1]: # Moon
        voice_lang = "en-GB"
        voice_name = "en-GB-Wavenet-B"
        voice_gender = texttospeech.enums.SsmlVoiceGender.MALE
    elif agent == agent_names[2]: # Saturn
        voice_lang = "en-GB"
        voice_name = "en-GB-Wavenet-A"
        voice_gender = texttospeech.enums.SsmlVoiceGender.FEMALE
    elif agent == agent_names[3]: # BASIL
        voice_lang = "en-US"
        voice_name = "en-US-Wavenet-C"
        voice_gender = texttospeech.enums.SsmlVoiceGender.FEMALE
    elif agent == agent_names[4]: # SUNFLOWER
        voice_lang = "en-US"
        voice_name = "en-US-Wavenet-B"
        voice_gender = texttospeech.enums.SsmlVoiceGender.MALE
    elif agent == agent_names[1] + "_" + agent_names[2]: # Moon & Saturn
        voice_lang = "en-US"
        voice_name = "en-US-Wavenet-A"
        voice_gender = texttospeech.enums.SsmlVoiceGender.NEUTRAL # TODO: make new double voice recordings

    # set voice parameters
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=voice_lang,
        name=voice_name,
        ssml_gender=voice_gender)

    return voice

# set path using audio content, agent name
def set_audio_name(phrase, agent, scenario):
    MAXCHARS = 40 # max num chars in audio file name
    num_chars = MAXCHARS
    if (len(phrase) < MAXCHARS): # if less than 40 chars
        num_chars = len(phrase)

    audio_file_name = agent + "_" + phrase[0:num_chars - 1]
    audio_file_name = audio_file_name.replace(" ", "_").replace("\'", "-")
    
    return audio_file_name + ".mp3"

# return context in string
def get_context(context_char):
    context = ""
    if(context_char == "c"):
        context = "clinic"
    elif(context_char == "s"):
        context = "store"
    elif(context_char == "h"):
        context = "hotel"
    return context

# return agent configuration in string
def get_config(config_num):
    config = ""
    if(config_num == 1):
        config = "singular"
    elif(config_num == 2):
        config = "psa"
    elif(config_num == 3):
        config = "my"
    return config

# create new text file with P1 and P2 replaced with actual participant names to read from
def make_text_with_names(script_path):
    # convert docx to txt file
    text = docx2txt.process(script_path + ".docx")
    f = open(script_path + ".txt", 'w+')
    f.write(text)
    f.close()

    # read template file (with P1 and P2)
    f = open(script_path + ".txt",'r')
    filedata = f.read()
    f.close()

    # replace P1, P2 with actual participant names
    newdata = filedata.replace("P1", participant_1).replace("P2", participant_2)

    # write to copy of original file
    f = open(script_path + "_copy.txt",'w+')
    f.write(newdata)
    f.close()

# create all audio files for this scenario from .txt file
def make_scenario_files(script_path, scenario_name):
    # read each line in file
    f = open(script_path + "_copy.txt", "r")
    f1 = f.readlines()

    for line in f1:
        split_line = line.split(": ")
        speaker_list = split_line[0].split(' ')
        # if line is Robot's line, make audio file
        if (len(speaker_list) > 1):
            if speaker_list[1] == "ROBOT": # 1 if numbered
                agent_name_parentheses = speaker_list[2] # 2 if numbered
                agent_name = agent_name_parentheses.replace('(', '').replace(')', '').upper()
                make_audio_file(split_line[1], agent_name, scenario_name)

def main():
    # input text from file, not interface
    global fromFile
    fromFile = True

    # take command-line arguments of file name and participant names
    global participant_1
    global participant_2
    participant_1 = sys.argv[1]
    participant_2 = sys.argv[2]

    # for each scenario from command line arguments
    for index_scenario in range(3, len(sys.argv)):
        arg_scenario = sys.argv[index_scenario] # ex. c1
        context = get_context(arg_scenario[0]) # ex. clinic
        config = get_config(int(arg_scenario[1], 10)) # ex. singular
        scenario_name = context + "_" + config # ex. clinic_singular

        # make folder for all audio files of scenario
        os.makedirs("soundfiles/" + participant_1 + "_" + participant_2 + "/" + scenario_name)
        
        # path to raw .docx scripts
        script_path = "scripts" + "/" + context + "/" + scenario_name

        # create .txt file from original .docx files with names replaced
        make_text_with_names(script_path)

        # create all audio files for this scenario in appropriate folders
        make_scenario_files(script_path, scenario_name)

if __name__ == '__main__':
    main()
