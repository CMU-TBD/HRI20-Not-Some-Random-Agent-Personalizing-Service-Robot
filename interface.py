#!/usr/bin/env python

# Copyright (c) 2019 Sam Reig & Janet Wang
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

# NOTE: for audio to play, NO NEW LINE CHARACTERS IN INPUT TEXT BOX!

import sys
from tkinter import *
import pyglet
from texttospeechwizard import make_audio_file, agent_names

window = Tk()

window.title("Text-To-Speech")
window.geometry('600x300')

# write agent voice selection
def select_agent():
   selection = "Audio file will be created in " + str(var.get() + "'s voice.")
   voiceLabel.config(text=selection)

# retrieve text and make audio file
def process_text():
    audiocontent = phrase.get("1.0", END)
    phraseLabel.configure(text="Created audio file in soundfiles folder!")
    make_audio_file(audiocontent, str(var.get()))

# create and label text box
phraseLabel = Label(window, text="Enter text to create its audio file below:")
phraseLabel.grid(column=0, row=0)

phrase = Text(window, width=80, height=5, bg="whitesmoke")
phrase.grid(column=0, row=1)

# create agent voice options buttons
var=StringVar()
for name in agent_names:
    nameButton = Radiobutton(window, text=name, value=name, variable=var, command=select_agent)
    nameButton.grid(column=0, row=agent_names.index(name)+2)

voiceLabel=Label(window)
voiceLabel.grid(column=0, row=19)

# create button for making audio file (processText)
makeButton = Button(window, text="Make audio file", command=process_text)
makeButton.grid(column=0, row=20)

window.mainloop()

