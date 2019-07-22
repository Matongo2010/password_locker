import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        setup before a test is run
        '''
        self.new_credential = Credentials("facebook", "justineadriano@gmail", "matongo2010")