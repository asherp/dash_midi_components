from jupyter_dash import JupyterDash

from dash import Dash

from dash.dependencies import Input, Output, ClientsideFunction

# +
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = JupyterDash(__name__,
                  external_stylesheets=external_stylesheets,
                  external_scripts=['https://surikov.github.io/webaudiofont/npm/dist/WebAudioFontPlayer.js',
                                    'https://surikov.github.io/webaudiofontdata/sound/0250_SoundBlasterOld_sf2.js',
                                    'https://surikov.github.io/webaudiofontdata/sound/0240_Chaos_sf2_file.js',])


# changeInstrument('https://surikov.github.io/webaudiofontdata/sound/0290_Aspirin_sf2_file.js','_tone_0290_Aspirin_sf2_file');

simple_pitch = html.Div(children=[
    html.Div([
        html.Div([
            html.Div('preset'),
            dcc.Dropdown(
                id='preset',
                options=[
                    {'label': 'piano',
                     'value': '0250_SoundBlasterOld_sf2'},
                    {'label': 'guitar',
                     'value': '0240_Chaos_sf2_file'},
                ],
                value='0250_SoundBlasterOld_sf2',
                clearable=False,
            )], className='three columns'),
        html.Div([
            html.Div('when'),
            dcc.Input(id='when', value=0, type='number'),
            ], className='two columns'),
        html.Div([
            html.Div('pitch'),
            dcc.Input(id='pitch', value=42, type='number')
            ], className='two columns'),
        html.Div([
            html.Div('duration'),
            dcc.Input(id='duration', value=2, type='number')
            ], className='two columns'),
        html.Div([
            html.Div('volume'),
            dcc.Input(id='volume', value=1, type='number', step=.1),
            ], className='two columns')
        ], className='row'),
    html.Div([
        html.Div(
            children=json.dumps(dict(
                path='https://surikov.github.io/webaudiofontdata/sound/0240_FluidR3_GM_sf2_file.js',
                name='_tone_0240_FluidR3_GM_sf2_file')), 
            id='change-input',
            className='three columns')
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


app.clientside_callback(
    ClientsideFunction(namespace='dash_midi', function_name='play'),
    Output('out-component', 'children'),
    Input('preset', 'value'),
    Input('when', 'value'),
    Input('pitch', 'value'),
    Input('duration', 'value'),
    Input('volume', 'value'),
)

# app.clientside_callback(
#     ClientsideFunction(namespace='dash_midi', function_name='changeInstrument'),
#     Output('out-component2', 'children'),
#     Input('change-input', 'children'),
# )

app.layout = html.Div([simple_pitch])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, mode='external', debug=True)
# -

