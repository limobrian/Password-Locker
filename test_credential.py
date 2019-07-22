import pyperclip
import unittest
from credential import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):
        
        self.new_credential = Credential("snapchat","brian","9364brian")

    def tearDown(self):
        Credential.credential_list = []
        
   
if __name__ == '__main__':
    unittest.main()