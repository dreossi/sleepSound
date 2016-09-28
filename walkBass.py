import chord
import scale
import midi

import random
from random import randint


#Generate chord line
pianoChords = [];
pianoTimes = [0];
pianoDurations = [];

#Generate bass line
bassNotes = [];
bassTimes = [0];
bassDurations = [];


for k in range(0,8):

    root = random.choice([60,65,67])

    iim7 = chord.getMinChord(root+2)
    V7 = chord.getMajChord(root+7-12)
    I7 = chord.getMajChord(root)
    chords = [iim7,V7,I7,I7]
    
    pianoChords.append(iim7)
    pianoChords.append(V7)
    pianoChords.append(I7)
    pianoChords.append(I7)
    
    pianoTimes.append(pianoTimes[-1]+4)
    pianoTimes.append(pianoTimes[-1]+4)
    pianoTimes.append(pianoTimes[-1]+4)
    pianoTimes.append(pianoTimes[-1]+4)
    
    pianoDurations.append(4)
    pianoDurations.append(4)
    pianoDurations.append(8)
    pianoDurations.append(0)

    iim7Scale = scale.getMinScale(root+2-24)
    V7Scale = scale.getMajScale(root+7-24)
    I7Scale = scale.getMajScale(root-24)
    scales = [iim7Scale,V7Scale,I7Scale,I7Scale]   

    for j in range(0,4):
        for i in range(0,4):
            # First note
            actScale = scales[i]

            bassNotes.append(chord.getRoot(chords[i]))
            bassTimes.append(bassTimes[-1]+1)
            bassDurations.append(1)

            # Second note
            bassNotes.append(actScale[randint(0,7)])
            bassTimes.append(bassTimes[-1]+1)
            bassDurations.append(1)

            # Third note
            bassNotes.append(actScale[randint(0,7)])
            bassTimes.append(bassTimes[-1]+1)
            bassDurations.append(1)

            # Forth note
            chromatic = random.choice([-1,+1,-2,+2,-7,+7])
            bassNotes.append(chord.getRoot(chords[(i+1)%4]) + chromatic)
            bassTimes.append(bassTimes[-1]+1)
            bassDurations.append(1)


midi.genMidiChord(pianoChords,pianoTimes,pianoDurations,"piano")
midi.genMidiMelody(bassNotes,bassTimes,bassDurations,"bass")
