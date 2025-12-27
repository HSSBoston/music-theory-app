import streamlit as st
import random
from music21 import *

st.title("Music Theory Helper")

listNumOfAccidentals = [0,1,2,3,4,5,6,7]
listSharpOrFlat = ["sharps", "flats"]

accidentals = random.choice(listNumOfAccidentals)
sharpOrFlat = random.choice(listSharpOrFlat)

st.subheader("What is the name of the key signature with "+str(accidentals)+" "+sharpOrFlat)

if sharpOrFlat == "sharps":
    ks = key.KeySignature(accidentals);
    key = ks.asKey()
    st.text(key)
else:
    ks = key.KeySignature(-accidentals);
    key = ks.asKey()
    st.text(key)
    
st.subheader("What is the relative minor of "+str(key))

st.text(key.relative)

st.subheader("What is the parallel minor of "+str(key))

st.text(key.parallel)


