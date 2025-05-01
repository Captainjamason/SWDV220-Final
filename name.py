###   SWDV 220 - Wk8 Final Project
###   JPD - 2025
###   name.py

import pyphen
import random
DIC = pyphen.Pyphen(lang='en')
CONSTS = "bcdfghjklmnpqrstvwxyz"


def genName(entry1, entry2):
    # Debug output.
    print(f"Generating name for {entry1} and {entry2}...")
    # Split into lists of syllables.
    syl1 = DIC.inserted(entry1).split("-")
    syl2 = DIC.inserted(entry2).split("-")
    # Randomly select a syllable from each list.
    part1 = random.choice(syl1)
    part2 = random.choice(syl2)
    # If the first part ends with a consonant, add a vowel.
    if part1[-1:] in CONSTS:
        part1 += "i"
    # Splice the two parts together
    name = part1 + part2
    # Debug output.
    print(f"Generated name: {name}")