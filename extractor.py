import math


class PitchExtractor:
    def __init__(self, file_path):
        self.load_midi(file_path)

    def load_midi(self, file_path):
        with open(file_path, 'rb') as midi_file:
            self._parse_header(midi_file)
            self._track_data_hex = midi_file.read().hex()

            if (self._file_format) == 1:
                self._remove_tempo_track()

    def _parse_header(self, midi_file):
        leader = midi_file.read(4)
        if leader != b'MThd':
            raise ValueError('Invalid file type')

        track_info = midi_file.read(10)
        self._file_format = int.from_bytes(track_info[4: 6], 'big')

    def _remove_tempo_track(self):
        track_header = '4d54726b'

        # Start loop after current track header
        for i in range(8, len(self._track_data_hex), 2):
            if self._track_data_hex[i:i+8] == track_header:
                # Slice off first track
                self._track_data_hex = self._track_data_hex[i:]
                break

    def _get_note_names(self, pitch_list):
        notes = []
        pitch_names = ['C', 'C#', 'D', 'D#', 'E',
                       'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        for pitch in pitch_list:
            octave = math.floor(pitch / 12)
            pitch_name = pitch_names[pitch - (12 * octave)]

            notes.append(pitch_name + str(octave))

        return notes

    def get_pitches(self, note_names=False):
        pitches = []

        for i in range(0, len(self._track_data_hex), 2):
            is_pitch = self._track_data_hex[i] == '9'
            is_note_on = self._track_data_hex[i + 4: i + 6] != '00'

            if is_pitch and is_note_on:
                pitch_hex = self._track_data_hex[i + 2: i + 4]
                pitches.append(int(pitch_hex, 16))

        if note_names:
            return self._get_note_names(pitches)

        return pitches

    def get_file_format(self):
        return self._file_format
