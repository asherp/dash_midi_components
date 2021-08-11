# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from html.parser import HTMLParser
import urllib
from collections import defaultdict 

class MidiIndexParser(HTMLParser):
    def __init__(self, base="https://surikov.github.io/webaudiofontdata/sound/"):
        
        super().__init__()
        self._tab = ''
        self.last_instrument = None
        self.instruments = defaultdict(dict)
        
        result = urllib.request.urlopen(base).read()
        self.feed(result.decode("utf-8"))
        
    def handle_starttag(self, tag, attrs):
        self._tab = self._tab + '\t'
        if tag == 'a':
            category, instrument = self.last_instrument
            for _ in attrs:
                if 'href' in _:
                    html_path = _[1]
                    preset = html_path.split('.html')[0]
                    self.instruments[category][instrument].append(
                        {'_tone_' + preset: preset + '.js'})

    def handle_endtag(self, tag):
        self._tab = self._tab[:-2]

    def handle_data(self, data):
        if ':' in data:
            instrument, category = [_.strip() for _ in data.split(':')]
            self.instruments[category][instrument] = []
            self.last_instrument = category, instrument
        elif 'Drums' in data:
            instrument, category = 'Drums', 'Drums'
            self.instruments[category][instrument] = []
            self.last_instrument = category, instrument


# %%
instruments = MidiIndexParser().instruments
instruments


# %%
class MidiDrumParser(HTMLParser):
    def __init__(self, base):
        super().__init__()
        self._tab = ''
        self.last_tag = None
        self.instruments = []
        
        result = urllib.request.urlopen(base).read()
        self.feed(result.decode("utf-8"))
    
    def handle_starttag(self, tag, attrs):
#         print(tag, attrs, end='')
        self.last_tag = tag
        pass
    
    def handle_endtag(self, tag):
#         print(tag)
        pass
    
    def handle_data(self, data):
        if (self.last_tag == 'a') & ('.js' in data):
            _, _, fname, _, var = [_.strip() for _ in data.split(' ')]
            self.instruments.append(dict(var=var, file=fname))


drums = MidiDrumParser('https://surikov.github.io/webaudiofontdata/sound/drums_6_SBLive_sf2Brush.html')

# %%
drums.instruments

# %% [markdown]
# What are your plans for Keysend script? DLCs? I'm interested in p2p

# %%
