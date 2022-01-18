import itertools
from unittest import TestCase
from unittest.mock import patch
import io
from game import draw_map as draw_map


class TestDrawMap(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw_1x1_map(self, map_output):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        rows = 1
        columns = 1
        separator = itertools.repeat("-", columns * 5)
        separator = "".join(separator)
        expected = "\n(!!!)\n" + separator + "\n"
        draw_map(character, rows, columns)
        actual = map_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw_2x2_map(self, map_output):
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        rows = 2
        columns = 2
        separator = itertools.repeat("-", columns * 5)
        separator = "".join(separator)
        expected = """
($$$)($$$)
($$$)(!!!)\n""" + separator + "\n"
        draw_map(character, rows, columns)
        actual = map_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw_3x3_map(self, map_output):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        rows = 3
        columns = 3
        separator = itertools.repeat("-", columns * 5)
        separator = "".join(separator)
        expected = """
(!!!)($$$)($$$)
($$$)($$$)($$$)
($$$)($$$)($$$)\n""" + separator + "\n"
        draw_map(character, rows, columns)
        actual = map_output.getvalue()
        self.assertEqual(expected, actual)

    def test_draw_map_and_character_dictionary_is_not_changed(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        character_copy = {'X-coordinate': 0, 'Y-coordinate': 0}
        rows = 1
        columns = 1
        draw_map(character, rows, columns)
        self.assertEqual(character, character_copy)
