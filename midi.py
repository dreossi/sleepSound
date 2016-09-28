from midiutil.MidiFile import MIDIFile

def genMidiChord(chords,times,durations,filename):
    # create your MIDI object
    mf = MIDIFile(1)     # only 1 track
    track = 0   # the only track

    time = 0    # start at the beginning
    mf.addTrackName(track, time, filename)
    mf.addTempo(track, time, 120)

    # add some notes
    channel = 0
    volume = 100
    
    for i in range(len(chords)): 
        chord = chords[i]
        for note in chord:
            pitch = note           # C4 (middle C)
            time = times[i]             # start on beat 0
            duration = durations[i]         # 1 beat long
            mf.addNote(track, channel, pitch, time, duration, volume)


    # write it to disk
    with open(filename+'.mid', 'wb') as outf:
        mf.writeFile(outf)
        
        
def genMidiMelody(notes,times,durations,filename):
    # create your MIDI object
    mf = MIDIFile(1)     # only 1 track
    track = 0   # the only track

    time = 0    # start at the beginning
    mf.addTrackName(track, time, filename)
    mf.addTempo(track, time, 120)

    # add some notes
    channel = 0
    volume = 100
    
    print notes
    print times
    
    for i in range(len(notes)): 
        pitch = notes[i]          # C4 (middle C)
        time = times[i]             # start on beat 0
        duration = durations[i]         # 1 beat long
        mf.addNote(track, channel, pitch, time, duration, volume)


    # write it to disk
    with open(filename+'.mid', 'wb') as outf:
        mf.writeFile(outf)