from music21 import *
import random

noteList = ["C5","C#5","D-5","D5","D#5","E-5","E5","F-5","F5","F#5","G-5","G5","G#5","A-5","A5","A#5","B-5","B5","C-5"]

root = note.Note(random.choice(noteList))
third = root.transpose("M3")
fifth = third.transpose("m3")

randomInt = random.randint(0,1)
if randomInt < 0.5:
    seventh = fifth.transpose("M3")
    c = chord.Chord([root, third, fifth,seventh])
    inversionList = [0, 1, 2, 3]
else:
    c = chord.Chord([root, third, fifth])
    inversionList = [0, 1, 2]

c.inversion(random.choice(inversionList))

print("What is the inversion of the following chord: ")
print(c.pitchNames)
print(c.inversionText())
# c2 = chord.Chord("C3 E3 G3 B-3")
# kc = key.Key("C")
# rn = roman.romanNumeralFromChord(c2, kc)
# print(rn.function)

