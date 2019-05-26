import unittest
from extractor import PitchExtractor


class TestExtractor(unittest.TestCase):
    def test_load_midi_file_type_error(self):
        """ Raises a value error if not a midi file """
        with self.assertRaises(ValueError):
            self.pxt = PitchExtractor('tests/test_files/not_midi.mid')

    def test_pitches_with_midi_values(self):
        """ Should return a list of midi values"""
        self.pxt = PitchExtractor('tests/test_files/twinkle.mid')
        expected_result = [60, 60, 67, 67, 69,
                           69, 67, 65, 65, 64, 64, 62, 62, 60]

        self.assertEqual(self.pxt.pitches(), expected_result)

    def test_pithes_with_note_names(self):
        """ Should return a list note names"""
        self.pxt = PitchExtractor('tests/test_files/twinkle.mid')
        expected_result = ['C5', 'C5', 'G5', 'G5', 'A5', 'A5',
                           'G5', 'F5', 'F5', 'E5', 'E5', 'D5', 'D5', 'C5']

        self.assertEqual(self.pxt.pitches(note_names=True), expected_result)

    def test_get_note_names(self):
        """ Take in a list of midi values and return a list of note names"""
        self.pxt = PitchExtractor('tests/test_files/twinkle.mid')
        input = [60, 60, 67, 67, 69,
                 69, 67, 65, 65, 64, 64, 62, 62, 60]
        expected_result = ['C5', 'C5', 'G5', 'G5', 'A5', 'A5',
                           'G5', 'F5', 'F5', 'E5', 'E5', 'D5', 'D5', 'C5']

        self.assertEqual(self.pxt._get_note_names(input), expected_result)


if __name__ == '__main__':
    unittest.main()
