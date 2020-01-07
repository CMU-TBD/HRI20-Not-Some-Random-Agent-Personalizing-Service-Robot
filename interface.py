#!/usr/bin/env python

# MIT License

# Copyright (c) 2020 CMU-TBD

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

