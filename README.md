
# Dash Midi Components

Generates client-side midi for plotly dash components, providing data-driven audio in the form of midi.

`Dash Midi Componets` is built on [webaudiofont](https://surikov.github.io/webaudiofont/), a pure javascript midi library that includes a large collection of midi intrustruments. `Dash Midi Components` parses the html files from webaudiofont and makes it easy to use them through dash clientside callbacks. 

## Usage

To see the demo, navigate to `dash_midi_components` and run `midi_test.py`

```console
cd dash_midi_components
python midi_test.py
```


## Notes

The first time an instrument loads, there will be a brief pause while the instrument source is loaded into your browser. You may preload instruments by including their paths to the dash object's `external_scripts`.

Custom samples may be defined by following this [tutorial](https://surikov.github.io/webaudiofont/examples/customsample.html).

## Catalogue

The webaudiofont library includes a total of 175 instruments with 5226 voicings, divided among the following categories shown below.

Piano
 Acoustic Grand Piano (8)
 Bright Acoustic Piano (8)
 Electric Grand Piano (8)
 Honky-tonk Piano (8)
 Electric Piano 1 (8)
 Electric Piano 2 (8)
 Harpsichord (8)
 Clavinet (8)
Chromatic Percussion
 Celesta (8)
 Glockenspiel (8)
 Music Box (8)
 Vibraphone (8)
 Marimba (8)
 Xylophone (8)
 Tubular Bells (8)
 Dulcimer (8)
Organ
 Drawbar Organ (8)
 Percussive Organ (8)
 Rock Organ (8)
 Church Organ (8)
 Reed Organ (8)
 Accordion (8)
 Harmonica (8)
 Tango Accordion (8)
Guitar
 Acoustic Guitar (nylon) (8)
 Acoustic Guitar (steel) (8)
 Electric Guitar (jazz) (8)
 Electric Guitar (clean) (8)
 Electric Guitar (muted) (8)
 Overdriven Guitar (8)
 Distortion Guitar (8)
 Guitar Harmonics (8)
Bass
 Acoustic Bass (8)
 Electric Bass (finger) (8)
 Electric Bass (pick) (8)
 Fretless Bass (8)
 Slap Bass 1 (8)
 Slap Bass 2 (8)
 Synth Bass 1 (8)
 Synth Bass 2 (8)
Strings
 Violin (8)
 Viola (8)
 Cello (8)
 Contrabass (8)
 Tremolo Strings (8)
 Pizzicato Strings (8)
 Orchestral Harp (8)
 Timpani (8)
Ensemble
 String Ensemble 1 (8)
 String Ensemble 2 (8)
 Synth Strings 1 (8)
 Synth Strings 2 (8)
 Choir Aahs (8)
 Voice Oohs (8)
 Synth Choir (8)
 Orchestra Hit (8)
Brass
 Trumpet (8)
 Trombone (8)
 Tuba (8)
 Muted Trumpet (8)
 French Horn (8)
 Brass Section (8)
 Synth Brass 1 (8)
 Synth Brass 2 (8)
Reed
 Soprano Sax (8)
 Alto Sax (8)
 Tenor Sax (8)
 Baritone Sax (8)
 Oboe (8)
 English Horn (8)
 Bassoon (8)
 Clarinet (8)
Pipe
 Piccolo (8)
 Flute (8)
 Recorder (8)
 Pan Flute (8)
 Blown bottle (8)
 Shakuhachi (8)
 Whistle (8)
 Ocarina (8)
Synth Lead
 Lead 1 (square) (8)
 Lead 2 (sawtooth) (8)
 Lead 3 (calliope) (8)
 Lead 4 (chiff) (8)
 Lead 5 (charang) (8)
 Lead 6 (voice) (8)
 Lead 7 (fifths) (8)
 Lead 8 (bass + lead) (8)
Synth Pad
 Pad 1 (new age) (8)
 Pad 2 (warm) (8)
 Pad 3 (polysynth) (8)
 Pad 4 (choir) (8)
 Pad 5 (bowed) (8)
 Pad 6 (metallic) (8)
 Pad 7 (halo) (8)
 Pad 8 (sweep) (8)
Synth Effects
 FX 1 (rain) (8)
 FX 2 (soundtrack) (8)
 FX 3 (crystal) (8)
 FX 4 (atmosphere) (8)
 FX 5 (brightness) (8)
 FX 6 (goblins) (8)
 FX 7 (echoes) (8)
 FX 8 (sci-fi) (8)
Ethnic
 Sitar (8)
 Banjo (8)
 Shamisen (8)
 Koto (8)
 Kalimba (8)
 Bagpipe (8)
 Fiddle (8)
 Shanai (8)
Percussive
 Tinkle Bell (8)
 Agogo (8)
 Steel Drums (8)
 Woodblock (8)
 Taiko Drum (8)
 Melodic Tom (8)
 Synth Drum (8)
 Reverse Cymbal (8)
Sound effects
 Guitar Fret Noise (8)
 Breath Noise (8)
 Seashore (8)
 Bird Tweet (8)
 Telephone Ring (8)
 Helicopter (8)
 Applause (8)
 Gunshot (8)
Drums
 Bass Drum 2 (47)
 Bass Drum 1 (47)
 Side Stick/Rimshot (47)
 Snare Drum 1 (47)
 Hand Clap (47)
 Snare Drum 2 (47)
 Low Tom 2 (47)
 Closed Hi-hat (47)
 Low Tom 1 (47)
 Pedal Hi-hat (47)
 Mid Tom 2 (47)
 Open Hi-hat (47)
 Mid Tom 1 (47)
 High Tom 2 (47)
 Crash Cymbal 1 (47)
 High Tom 1 (47)
 Ride Cymbal 1 (47)
 Chinese Cymbal (47)
 Ride Bell (47)
 Tambourine (47)
 Splash Cymbal (47)
 Cowbell (47)
 Crash Cymbal 2 (47)
 Vibra Slap (47)
 Ride Cymbal 2 (47)
 High Bongo (47)
 Low Bongo (47)
 Mute High Conga (47)
 Open High Conga (47)
 Low Conga (47)
 High Timbale (47)
 Low Timbale (47)
 High Agogo (47)
 Low Agogo (47)
 Cabasa (47)
 Maracas (47)
 Short Whistle (47)
 Long Whistle (47)
 Short Guiro (47)
 Long Guiro (47)
 Claves (47)
 High Wood Block (47)
 Low Wood Block (47)
 Mute Cuica (47)
 Open Cuica (47)
 Mute Triangle (47)
 Open Triangle (47)