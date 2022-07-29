import json
from unittest import TestCase, mock
from unittest.mock import patch, mock_open

from tests.stubs import (
    FakeTranslationObj
)
from scripts.translator import (
    translate_csv,
    translate_txt
)

class TestTranslator(TestCase):
    @patch("scripts.translator.open", mock_open(read_data="bad data"), create=False)
    @patch('scripts.translator.Translator', return_value=FakeTranslationObj) # Mocks Translator().
    def test_basic(self, mock_translation, mock_file_opens):
        # mock_file_opens.side_affect=['data', mock_open(read_data="bad data")]
        
        # import pdb; pdb.set_trace()
        # self.assertEqual(mock_file_opens(), 'data')

        # Mocks cmd to run script
        with mock.patch('sys.argv', ['run-txt', 'file1.txt', 'file2.txt']):
            # with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            translate_txt()

    # @patch('scripts.translator.Translator', return_value=[666])
    # def test_command(self, mock_item):
    #     #will throw

    #     with mock.patch('sys.argv', ['run-txt']):
    #         import pdb; pdb.set_trace()
    #         translate_txt()