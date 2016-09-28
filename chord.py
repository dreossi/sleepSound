import midi

# Generate a major chord
def getMajChord(root):
    third = root + 4
    fifth = root + 7
    seventh = root + 11

    chord = [root, third, fifth, seventh]
    
    return chord

# Generate a minor chord
def getMinChord(root):
    third = root + 3
    fifth = root + 7
    seventh = root + 10

    chord = [root, third, fifth, seventh]
    
    return chord

# Generate the root of a chord
def getRoot(chord):    
    return chord[0]