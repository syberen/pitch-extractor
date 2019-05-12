# Pitch Extractor

A python module for extracting pitch datasets from midi files. Currently works only with type 0 midi files. 

### Usage
Load a midi file and get list of pitches:

```python
from extractor import PitchExtractor

xtr = PitchExtractor()
xtr.load_midi('beethoven.mid')

pitches = xtr.get_pitches()
```

To get a list of notes instead of notes instead of midi values use `xtr.get_pitches(note_names=True)`