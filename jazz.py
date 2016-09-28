import chord
import scale
import midi

from random import randint

root = 60

iim7 = chord.getMinChord(root+2)
V7 = chord.getMajChord(root+7-12)
I7 = chord.getMajChord(root)
chords = [iim7,V7,I7]

times = [0,4,8]
durations = [4,4,8]

iim7Scale = scale.getMinScale(root+2-24)
V7Scale = scale.getMajScale(root+7-24)
I7Scale = scale.getMajScale(root-24)

#Generate bass line
bassNotes = [];
bassTimes = [0];
bassDurations = [];


for j in range(0,4):
    for i in range(0,4):
        bassNotes.append(iim7Scale[randint(0,7)])
        bassTimes.append(bassTimes[-1]+1)
        bassDurations.append(1)
    
    
    for i in range(0,4):
        bassNotes.append(V7Scale[randint(0,7)])
        bassTimes.append(bassTimes[-1]+1)
        bassDurations.append(1)
    
    for i in range(0,8):
        bassNotes.append(I7Scale[randint(0,7)])
        bassTimes.append(bassTimes[-1]+1)
        bassDurations.append(1)



midi.genMidiChord(chords,times,durations,"piano")
midi.genMidiMelody(bassNotes,bassTimes,bassDurations,"bass")
