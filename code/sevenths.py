from music21 import *
import random

noteList = ["C5","C#5","D-5","D5","D#5","E-5","E5","F-5","F5","F#5","G-5","G5","G#5","A-5","A5","A#5","B-5","B5","C-5"]

root = note.Note(random.choice(noteList))

randomInt = random.randint(0,1)
if randomInt < 0.5:
    third = root.transpose("M3")
    major = True
    fifth = third.transpose("m3")
else:
    third = root.transpose("m3")
    major = False
    randomInt = random.randint(0,1)
    if randomInt < 0.5:
        fifth = third.transpose("M3")
        
    else:
        fifth = third.transpose("m3")
    
randomInt = random.randint(0,1)
if randomInt < 0.5:
    seventh = fifth.transpose("M3")
else:
    seventh = fifth.transpose("m3")
    
c = chord.Chord([root, third, fifth, seventh])
    
print("What type of seventh is the following chord?")
print(c.pitchNames)



if c.isDominantSeventh():
    print("Dominant Seventh")
elif c.isDiminishedSeventh():
    print("Diminished Seventh")
elif c.isHalfDiminishedSeventh():
    print("Half Diminished Seventh")
elif major:
    print("Major Seventh")
else:
    print("Minor Seventh")
    
