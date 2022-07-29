from unittest.mock import MagicMock
from scripts.utils import (
    load_fixture
)


class FakeTranslationObj(object):
    def __init__(self):
        self.text = 'dog'
        self.src = 'en'
        self.dest = 'es'
    
    @staticmethod
    def translate(*args, **kwargs):
        # return Translated(self.text, self.src, self.dest)
        return Translated(*args, **kwargs)


class Translated(object):
    def __init__(self, *args, **kwargs):
        # import pdb; pdb.set_trace()
        try:
            self.text = args[0]
        except IndexError as ke:
            self.text = 'perro'

        try:
            self.origin = args[1]
        except IndexError as ke:
            self.origin = 'dog'

        self.src = kwargs.get('src') if kwargs.get('src') else 'en'
        self.dest = kwargs.get('dest') if kwargs.get('dest') else 'es'


class FakeRequest(object):
    def __init__(self, status_code=200, response='response', text='text'):
        self.status_code = status_code
        self.response = response
        self.text = text
        self.reason = "testing!"
        self.url = "url"

    @staticmethod
    def json():
        return {}
