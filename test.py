import unittest
from extractor import PitchExtractor


class TestExtractor(unittest.TestCase):
    def setUp(self):
        self.pxt = PitchExtractor('midi_samples/twinkle.mid')

    def test_create_pitch_list(self):
        expected_result = [60, 60, 67, 67, 69,
                           69, 67, 65, 65, 64, 64, 62, 62, 60]

        self.assertEqual(self.pxt._create_pitch_list(), expected_result)

    def test_get_note_names(self):
        input = [60, 60, 67, 67, 69,
                 69, 67, 65, 65, 64, 64, 62, 62, 60]
        expected_result = ['C5', 'C5', 'G5', 'G5', 'A5', 'A5',
                           'G5', 'F5', 'F5', 'E5', 'E5', 'D5', 'D5', 'C5']

        self.assertEqual(self.pxt._get_note_names(input), expected_result)


if __name__ == '__main__':
    unittest.main()
