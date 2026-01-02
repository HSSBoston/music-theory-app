from music21 import *
import numpy as np
import random

RANDOM_SEED_NOTE = None #None or int
rng = np.random.default_rng(seed=RANDOM_SEED_NOTE)

P = np.array(
    [[0, 0.4, 0.4, 0.1, 0.1, 0, 0, 0],
     [0.3, 0, 0.4, 0.3, 0, 0, 0, 0],
     [0.1, 0.4, 0, 0.4, 0.1, 0, 0, 0],
     [0, 0.1, 0.4, 0, 0.4, 0.1, 0, 0],
     [0, 0, 0.3, 0.4, 0, 0.2, 0.1, 0],
     [0, 0, 0, 0.3, 0.4, 0, 0.3, 0],
     [0, 0, 0, 0.1, 0.1, 0.3, 0, 0.5]
     ])

#up to four accidentals only (to keep problems not too hard)
keysLettersList = ["C","G","D","A","E","F","B-","E-","A-","a","e","b","f#", "d", "g", "c","f"]
keyLetter = random.choice(keysLettersList)
k = key.Key(keyLetter)

if k.mode == "major":
  sc = scale.MajorScale(keyLetter)
else:
  sc = scale.MinorScale(keyLetter)

scalePitchNames = []
scaleMidi = []

start = k.tonic
start.octave = 4

for p in sc.getPitches():
  scalePitchNames.append(p.name)
  scaleMidi.append(p.midi)

n1 = note.Note(start)

randomInt = random.randint(0,1)
if randomInt < 0.5:
    timeSig = "4/4"
    length = 15
    n1.quarterLength = 1
    
    lastNote = note.Note(start)
    lastNote.queaterLength = 2
    length -= 2
else:
    timeSig = "6/8"
    length = 12
    randomInt = random.randint(0,1)
    if randomInt < 0.5:
        n1.quarterLength = 1
        length -= 1
    else:
        n1.quarterLength = 0.5
        length -= 0.5
        
    lastNote = note.Note(start)
    lastNote.quarterLength = 1.5
    length -= 1.5

melodyNoteList = [meter.TimeSignature(timeSig)]
melodyNoteList.append(n1)

temp = n1
while length > 0:
    newNoteSD = rng.choice(["1", "2", "3", "4", "5", "6", "7", "8"], p=P[scalePitchNames.index(temp.name)])
    newNote = note.Note(scalePitchNames[int(newNoteSD)-1])
    if newNote.name == k.getLeadingTone().name and keyLetter.islower():
        newNote.transpose(-1)
        

    if timeSig == "4/4":
        
        
            
        randomInt = random.randint(0,1)
        if randomInt < 0.4:
            newNote.quarterLength = 1
        elif randomInt < 0.7:
            newNote.quarterLength = 0.5
        elif randomInt < 0.9:
            newNote.quarterLength = 1.5
        else:
            newNote.quarterLength = 2
        
        if length - newNote.quarterLength < 0:
            newNote.quarterLength = length
            
        length -= newNote.quarterLength
        
    else:
        
        randomInt = random.randint(0,1)
        if randomInt < 0.3:
            newNote.quarterLength = 0.5
        elif randomInt < 0.6:
            newNote.quarterLength = 1
        elif randomInt < 0.7:
            newNote.quarterLength = 0.75
        elif randomInt < 0.8:
            newNote.quarterLength = 1.5
        else:
            newNote.quarterLength = 0.25
        
        if length - newNote.quarterLength < 0:
            newNote.quarterLength = length
            
        length -= newNote.quarterLength
    
    melodyNoteList.append(newNote)
    temp = newNote

melodyNoteList.append(lastNote)
melody = stream.Stream(melodyNoteList)
melody.show()