from music21 import *

c = key.Key("C")
b = note.Note("B")
if b.name == c.getLeadingTone().name:
    print("True")