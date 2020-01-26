# Pitch Extractor

A python module for extracting pitch datasets from midi files.

### Usage
Load a midi file and get list of pitches:

```python
from extractor import PitchExtractor

pxt = PitchExtractor('midi_samples/twinkle.mid')

pxt.get_pitches() # [60, 60, 67, 67, 69, 69, 67, 65, 65, 64, 64, 62, 62, 60]
```

To get a list of notes instead of notes instead of midi values use 
```python
pxt.get_pitches(note_names=True) # ['C5', 'C5', 'G5', 'G5', 'A5', 'A5', 'G5', 'F5', 'F5', 'E5', 'E5', 'D5', 'D5', 'C5']
```

Check whether the loaded midi file has format 0, 1 or 2:
```python
pxt.get_file_format() # 0
```