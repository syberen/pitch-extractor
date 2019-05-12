import math

class PitchExtractor:
    def __init__(self, file_path):
        if file_path:
            self.load_midi(file_path)

    def load_midi(self, file_path):
        with open(file_path, 'rb') as midi_file:
            leader = midi_file.read(4)
            if leader != b'MThd':
                raise ValueError('Invalid file type')

            data_hex_bytes = midi_file.read().hex()
            pitches = self._parse_hex_bytes(data_hex_bytes)

            self._pitches = pitches

    def _parse_hex_bytes(self, data):
        pitches = []

        for index, byte in enumerate(data):
            is_pitch = index % 2 == 0 and byte == '9'
            is_note_on = data[index + 4 : index + 6] != '00'

            if is_pitch and is_note_on: 
                pitch_hex = data[index + 2 : index + 4]
                pitches.append(int(pitch_hex, 16))
                
        return pitches
        
    def _get_note_names(self, pitches):
        notes = []
        pitch_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        for pitch in pitches:
            octave = math.floor(pitch / 12)
            pitch_name = pitch_names[pitch - (12 * octave)]

            notes.append(pitch_name + str(octave))
          
        return notes
        
    def pitches(self, note_names=False):
        if not self._pitches:
            raise ValueError('No pitches found')

        if note_names:
            return self._get_note_names(self._pitches)

        return self._pitches

            