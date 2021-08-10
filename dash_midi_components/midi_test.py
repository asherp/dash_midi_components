# -*- coding: utf-8 -*-
# %load_ext autoreload
# %autoreload 2

from midi_loader import instruments

from jupyter_dash import JupyterDash

from dash import Dash

# +
# dcc.Dropdown?
# -

from dash.dependencies import Input, Output, ClientsideFunction

# +
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# preload one instrument from every category

app = JupyterDash(__name__,
                  external_stylesheets=external_stylesheets,
                  external_scripts=['https://surikov.github.io/webaudiofont/npm/dist/WebAudioFontPlayer.js',
                                    'https://surikov.github.io/webaudiofontdata/sound/0250_SoundBlasterOld_sf2.js',
                                    'https://surikov.github.io/webaudiofontdata/sound/0240_Chaos_sf2_file.js',])


cat_0 = list(instruments.keys())[0]
instr_type_0 = list(instruments[cat_0].keys())[0]
instr_0 = instruments[cat_0][instr_type_0][0]

simple_pitch = html.Div(children=[
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='category',
                options=[{'label': cat, 'value': cat} for cat in instruments.keys()],
                value=cat_0,
                clearable=False),
            dcc.Dropdown(
                id='instrument-type',
                options=[{'label': instr, 'value': instr} for instr in instruments[cat_0]],
                value=instr_type_0,
                clearable=False),
            dcc.Dropdown(
                id='preset',
                options=[{'label': _, 'value': _} for _ in instruments[cat_0][instr_type_0]],
                value=instr_0,
                clearable=False),
        ], className='three columns'),
        html.Div([
            html.Div('when'),
            dcc.Input(id='when', min=0, value=0, type='number'),
            ], className='two columns'),
        html.Div([
            html.Div('pitch'),
            dcc.Input(id='pitch', min=0, value=42, type='number')
            ], className='two columns'),
        html.Div([
            html.Div('duration'),
            dcc.Input(id='duration', min=0, value=2, type='number')
            ], className='two columns'),
        html.Div([
            html.Div('volume'),
            dcc.Input(id='volume', min=0, value=1, type='number', step=.1),
            ], className='two columns')
        ], className='row'),
    html.Div(id='out-component', children='True'),
    html.Div(id='out-component2', children='True'),
    ])


# audioContext - AudioContext
# target - a node to connect to, for example audioContext.destination
# preset - variable with the instrument preset
# when - when to play, audioContext.currentTime or 0 to play now, audioContext.currentTime + 3 to play after 3 seconds
# pitch - note pitch from 0 to 127, for example 2+12*4 to play D of fourth octave (use MIDI key for drums)
# duration - note duration in seconds, for example 4 to play 4 seconds
# volume - 0.0 <=1.0 volume (0 is ‘no value’, ‘no value’ is 1)
# slides - array of pitch bends

# queueWaveTable(audioContext, target, preset, when, pitch, duration, volume, slides)

@app.callback(
    Output('instrument-type', 'options'),
    Output('instrument-type', 'value'),
    Input('category', 'value'))
def fetch_instrument_types(cat):
    instrument_types_ = list(instruments[cat].keys())
    return [dict(label=_, value=_) for _ in instrument_types_], instrument_types_[0]

@app.callback(
    Output('preset', 'options'),
    Output('preset', 'value'),
    Input('category', 'value'),
    Input('instrument-type', 'value'))
def fetch_instruments(cat, instrument_type):
    instruments_ = list(instruments[cat][instrument_type])
    return [dict(label=_, value=_) for _ in instruments_], instruments_[0]

app.clientside_callback(
    ClientsideFunction(namespace='dash_midi', function_name='play'),
    Output('out-component', 'children'),
    Input('preset', 'value'),
    Input('when', 'value'),
    Input('pitch', 'value'),
    Input('duration', 'value'),
    Input('volume', 'value'),
)


app.layout = html.Div([simple_pitch])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, mode='external', debug=True)
# -

