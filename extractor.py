import math

class PitchExtractor:
    def load_midi(self, file_path):
        with open(file_path, 'rb') as midi_file:
            leader = midi_file.read(4)
            if leader != b'MThd':
                raise ValueError('Invalid file type')

            self.data_hex_bytes = midi_file.read().hex()

            self.parse_hex_file(self.data_hex_bytes)

    def parse_hex_file(self, data):
        pitches = []

        for index, byte in enumerate(data):
            is_pitch = index % 2 ==0 and byte == '9'
            is_note_on = data[index + 4 : index + 6] != '00'

            if is_pitch and is_note_on: 
                pitch_hex = data[index + 2 : index + 4]
                pitches.append(int(pitch_hex, 16))
                
        self.pitches = pitches
        
    def get_pitches(self, note_names=False):
        if not self.pitches:
            raise ValueError('No pitches found')

        if note_names:
            return self.get_note_names(self.pitches)

        return self.pitches
        
    def get_note_names(self, pitches):
        notes = []
        pitch_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        for pitch in pitches:
            octave = math.floor(pitch / 12)
            pitch_name = pitch_names[pitch - (12 * octave)]

            notes.append(pitch_name + str(octave))
          
        return notes

            