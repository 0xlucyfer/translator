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
from scripts.utils import multi_mock_open, FIXTURE_PATH

# from mock_open import MockOpen
mock_file_data = {
    "file1.txt": "some text 1",
    "file2.txt": "some text 2",
    # ... and so on ...
}


# @pytest.fixture()
# def mocked_open(mocker):
#     m = mocker.patch("builtins.open")
#     m.side_effect = partial(mocked_file, m)
#     m.assert_opened = partial(assert_opened, m)
#     return m

class TestTranslator(TestCase):

    # @patch("scripts.translator.open")
    # @patch("scripts.translator.open", mock_open(read_data='test')) # Mocks Translator().
    @patch('scripts.translator.Translator', return_value=FakeTranslationObj) # Mocks Translator().
    def test_basic(self, mock_translation):
        # mo.return_value.__enter__.return_value = mock_open(read_data='test')

        # Mocks cmd to run script
        with mock.patch('sys.argv', ['run-txt', 'nouns/spanish-nouns.txt', 'file2.txt']):
            # with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            with patch('scripts.translator.open', create=True) as mo:
                # mo.return_value = MagicMock()
                reads = ['text1', 'text2']
                mo.return_value.__enter__.return_value.read.side_effect = lambda: reads.pop(0)
        
                # m_file.read.side_effect = lambda: reads.pop(0)
                translate_txt()

    # @patch('scripts.translator.Translator', return_value=[666])
    # def test_command(self, mock_item):
    #     #will throw

    #     with mock.patch('sys.argv', ['run-txt']):
    #         import pdb; pdb.set_trace()
    #         translate_txt()