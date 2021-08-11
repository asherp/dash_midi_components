// -*- coding: utf-8 -*-
var AudioContextFunc = window.AudioContext || window.webkitAudioContext;
var audioContext = new AudioContextFunc();
var player=new WebAudioFontPlayer();
var instr=null;
var base = 'https://surikov.github.io/webaudiofontdata/sound/';

player.loader.decodeAfterLoading(audioContext, '_tone_0250_SoundBlasterOld_sf2');

var sound_library = {
  "_tone_0250_SoundBlasterOld_sf2": _tone_0250_SoundBlasterOld_sf2,
  }

// audioContext - AudioContext
// target - a node to connect to, for example audioContext.destination
// preset - variable with the instrument preset
// when - when to play, audioContext.currentTime or 0 to play now, audioContext.currentTime + 3 to play after 3 seconds
// pitch - note pitch from 0 to 127, for example 2+12*4 to play D of fourth octave (use MIDI key for drums)
// duration - note duration in seconds, for example 4 to play 4 seconds
// volume - 0.0 <=1.0 volume (0 is ‘no value’, ‘no value’ is 1)
// slides - array of pitch bends

// queueWaveTable(audioContext, target, preset, when, pitch, duration, volume, slides)


window.dash_clientside = Object.assign({}, window.dash_clientside, {
    dash_midi: {
        play: function(preset, path, when, pitch, duration, volume) {

            if (typeof window[preset] !== 'undefined') {
                console.log('variable ' + preset + ' exists!')
                player.queueWaveTable(
                    audioContext,
                    audioContext.destination,
                    window[preset],
                    audioContext.currentTime + parseInt(when),
                    Math.max(parseInt(pitch), 0),
                    Math.max(duration, 0),
                    Math.max(volume, 0));
                return false;
            } else {
                console.log('loading '+ preset + ' from ' + path);
                player.loader.startLoad(audioContext, path, preset);
                player.loader.waitLoad(function () {
                    instr=window[preset];
                player.queueWaveTable(
                    audioContext,
                    audioContext.destination,
                    window[preset],
                    audioContext.currentTime + parseInt(when),
                    Math.max(parseInt(pitch), 0),
                    Math.max(duration, 0),
                    Math.max(volume, 0));
                return false;
                });
            }

        },
    }
});


// changeInstrument('https://surikov.github.io/webaudiofontdata/sound/0290_Aspirin_sf2_file.js','_tone_0290_Aspirin_sf2_file');



