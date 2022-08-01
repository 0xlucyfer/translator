import json
from unittest import TestCase, mock
from unittest.mock import patch, MagicMock, mock_open
from tests.stubs import (
    FakeTranslationObj,
    FakeOpen
)
from scripts.translator import (
    translate_csv,
    translate_txt
)
from scripts.utils import FIXTURE_PATH
from unittest.mock import call

# import pdb; pdb.set_trace()
class TestTranslator(TestCase):
    @patch('scripts.translator.create_ordered_alpha_txt_files', return_value={})
    @patch('scripts.translator.open', new_callable=mock_open, read_data="aa\nbb")
    @patch('scripts.translator.Translator', return_value=FakeTranslationObj) # Mocks Translator().
    def test_translate_txt_files(self, mock_translation, mo, mock_COATF):
        '''
            Test file reading & writing in translate_txt.
        '''
        # Setup
        expected = [call('tests/fixtures/nouns/spanish-nouns.txt', 'r'), call('tests/fixtures/file2.txt', 'w')]

        with mock.patch('sys.argv', ['run-txt', 'nouns/spanish-nouns.txt', 'file2.txt']):
            # Set with open return values.
            handlers = [mo.return_value, mock_open(read_data="AA\nBB").return_value, mock_open(read_data="666\n666").return_value]
            mo.side_effect = handlers
            # Function under test
            translate_txt()

        actual = mo.call_args_list
        assert actual == expected
        assert mo.call_count == 2

    # @patch('scripts.translator.Translator', return_value=[666])
    # def test_command(self, mock_item):
    #     #will throw

    #     with mock.patch('sys.argv', ['run-txt']):
    #         import pdb; pdb.set_trace()
    #         translate_txt()