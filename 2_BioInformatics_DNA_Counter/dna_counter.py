import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna.jpg')

st.image(image, use_column_width = True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA !

***
""")

######################### INPUT BOX ############################
st.header('Enter DNA Sequence : ')

sequence_input = ">DNA Query\ngatcctccatatacaacggt \natctccacctcaggtttaga \ntctcaacaacggaaccattg"


sequence = st.text_area("Sequence input : ", sequence_input, height=150)
sequence = sequence.splitlines() # split sequence into seprate lines
sequence
sequence = sequence[1: ] # skip the sequence name ( first line. )
sequence = ''.join(sequence) # Concatnate list of string.

st.write("""
***
""")

## Print Input DNA Sequence 
st.header(" Input DNA Query is : ")
sequence

### DNA Nucleotide count
st.header(" OUTPUT DNA Nucleotide Count :")
st.subheader('1. Print Dictionary. ')               # 1 : OUTPUT : Print Dictionary

def DNA_nucleotide_count(seq):
    d = dict( [
        ('A', seq.count('a')),
        ('T', seq.count('t')),
        ('G', seq.count('g')),
        ('C', seq.count('c')),
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())
X

st.subheader('2. Print Plain Text. ')               # 2 : OUTPUT : Print Plain Text
st.write('There are  '+str(X['A'])+ ' adenine (A)')
st.write('There are  '+str(X['T'])+ ' thymine (T)')
st.write('There are  '+str(X['G'])+ ' adenine guanine (G)')
st.write('There are  '+str(X['C'])+ ' thymine cytosine (C)')



st.subheader('3. Print DataFrame. ')               # 3 : OUTPUT : Print DataFrame
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns= {'index': 'nucleotide'})
st.write(df)



st.subheader('4. Display Bar Chart ')               # 4 : OUTPUT : Bar chart Using Altaier
p = alt.Chart(df).mark_bar().encode(x='nucleotide', y='count')
p = p.properties(width=alt.Step(80))
st.write(p)