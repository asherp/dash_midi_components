from jupyter_dash import JupyterDash

from dash import Dash

from dash.dependencies import Input, Output, ClientsideFunction

# +
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = JupyterDash(__name__,
                  external_stylesheets=external_stylesheets,
                  external_scripts=['https://surikov.github.io/webaudiofont/npm/dist/WebAudioFontPlayer.js',
                                    'https://surikov.github.io/webaudiofontdata/sound/0250_SoundBlasterOld_sf2.js'])




simple_pitch = html.Div(children=[
    html.Div([
        html.Div([
            html.Div('preset'),
            dcc.Dropdown(
                id='preset',
                options=[
                    {'label': '_tone_0250_SoundBlasterOld_sf2', 'value': '_tone_0250_SoundBlasterOld_sf2'},
                ],
                value='_tone_0250_SoundBlasterOld_sf2',
            )], className='two columns'),
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
    html.Div(id='out-component', children='True')
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
    ClientsideFunction(
        namespace='dash_midi',
        function_name='play'
    ),
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

